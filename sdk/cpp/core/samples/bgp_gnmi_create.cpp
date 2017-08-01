#include <iostream>
#include <memory>
#include "../src/path_api.hpp"
#include "../src/gnmi_provider.hpp"
#include "ydk/crud_service.hpp"
#include "ydk_openconfig/openconfig_bgp.hpp"
#include "args_parser.h"

using namespace std;
using namespace ydk;


void print_paths(ydk::path::SchemaNode & sn)
{
    std::cout << sn.get_path() << std::endl;
    for(auto const& p : sn.get_children())
        print_paths(*p);
}

void config_bgp(openconfig::openconfig_bgp::Bgp* bgp)
{
    // Set the Global AS
    bgp->global->config->as = 65172;
    bgp->global->config->router_id = "1.2.3.4";
    
    //Commented because of XR 611 issue with OC identity
//  auto afi_safi = make_unique<openconfig_bgp::Bgp::Global::AfiSafis::AfiSafi>();
//  afi_safi->afi_safi_name = openconfig_bgp_types::L3Vpn_Ipv4_UnicastIdentity();
//  afi_safi->config->afi_safi_name = openconfig_bgp_types::L3Vpn_Ipv4_UnicastIdentity();
//  afi_safi->config->enabled = false;
//  afi_safi->parent = bgp->global->afi_safis.get();
//  bgp->global->afi_safis->afi_safi.push_back(move(afi_safi));

    auto neighbor = make_unique<openconfig::openconfig_bgp::Bgp::Neighbors::Neighbor>();
    neighbor->neighbor_address = "6.7.8.9";
    neighbor->config->neighbor_address = "6.7.8.9";
    neighbor->config->peer_as = 65001;
    neighbor->config->local_as = 65001;
    neighbor->config->peer_group = "IBGP";
    //neighbor->config->peer_type = "INTERNAL";
    //neighbor->config->remove_private_as = openconfig_bgp_types::Private_As_Remove_AllIdentity();
    neighbor->parent = bgp->neighbors.get();
    bgp->neighbors->neighbor.push_back(move(neighbor));

    auto peer_group = make_unique<openconfig::openconfig_bgp::Bgp::PeerGroups::PeerGroup>();
    peer_group->peer_group_name = "IBGP";
    peer_group->config->peer_group_name = "IBGP";
    //peer_group->config->auth_password = "password";
    peer_group->config->description = "test description";
    peer_group->config->peer_as = 65001;
    peer_group->config->local_as = 65001;
    //peer_group->config->peer_type = "INTERNAL";
    //peer_group->config->remove_private_as = openconfig_bgp_types::Private_As_Remove_AllIdentity();
    peer_group->parent = bgp->peer_groups.get();
    bgp->peer_groups->peer_group.push_back(move(peer_group));
}

int main(int argc, char* argv[])
{
    vector<string> args = parse_args(argc, argv);
    //for(int i = 0; i < argc; i++) 
    //    args.push_back(argv[i]);
    
    if(args.empty()) return 1;
    
    string host, username, password, port, address;
    username = args[0]; password = args[1]; host = args[2]; port = args[3];

    std::cout << "name: " << username << " pw: " << password << " host: " << host << " port: " << port << std::endl;

    address.append(host);
    address.append(":");
    address.append(port);

    bool verbose=(args[4]=="--verbose");
    if(verbose)
    {
            auto logger = spdlog::stdout_color_mt("ydk");
            logger->set_level(spdlog::level::debug);
    }

    try
    {
        ydk::path::Repository repo{"/usr/local/share/ydk/0.0.0.0\:50051/"};

        gNMIServiceProvider provider{repo, address};  

        CrudService crud{};

        auto bgp = make_unique<openconfig::openconfig_bgp::Bgp>();
        config_bgp(bgp.get());
        bool reply = crud.create(provider, *bgp);
        if(reply) cout << "Create operation success" << endl << endl; else cout << "Operation failed" << endl << endl;
    }
    catch(YCPPError & e)
    {
        cerr << "Error details: "<<e<<endl;
    }
    return 0;
}
