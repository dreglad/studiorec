# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  # For a complete reference, please see the online documentation at
  # https://docs.vagrantup.com.

  # Base box
  config.vm.box = "ubuntu/xenial64"

  # Network
  config.vm.network "forwarded_port", guest: 8080, host: 8080

  # Provider
  config.vm.provider "virtualbox" do |vb|
    vb.memory = "1024"
  end

  # Ansible provisioning
  config.vm.provision "ansible_local" do |ansible|
    ansible.playbook = "provisioning/playbook.yml"
    ansible.sudo = true
  end

  # Screen message
  config.vm.provision "shell", inline: <<-SHELL
    export DEBIAN_FRONTEND=noninteractive
    export LC_ALL=C
    echo "\nListo!\n  Para utilizar, apunta tu navegador hacia:\n\n"
    echo "    Frontend:\n      http://127.0.0.1:8080/\n\n    Backend:\n      http://127.0.0.1:8080/?edit"
    echo "           usuario: admin\n        contraseña: studiorec\n\n.\n"
  SHELL
end
