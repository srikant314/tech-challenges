Vagrant.configure("2") do |config|
  config.vm.define "master" do |master|
    master.vm.box = "ubuntu/trusty64"
    master.vm.hostname = 'master'
    master.vm.box_url = "ubuntu/trusty64"

    master.vm.network :private_network, ip: "192.168.56.101"

    master.vm.provider :virtualbox do |v|
      v.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
      v.customize ["modifyvm", :id, "--memory", 512]
      v.customize ["modifyvm", :id, "--name", "master"]
    end
  end

  config.vm.define "node1" do |node1|
    node1.vm.box = "ubuntu/trusty64"
    node1.vm.hostname = 'node1'
    node1.vm.box_url = "ubuntu/trusty64"

    node1.vm.network :private_network, ip: "192.168.56.102"

    node1.vm.provider :virtualbox do |v|
      v.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
      v.customize ["modifyvm", :id, "--memory", 512]
      v.customize ["modifyvm", :id, "--name", "node1"]
    end
  end
end
