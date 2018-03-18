<?php

use EasyCorp\Bundle\EasyDeployBundle\Deployer\DefaultDeployer;

return new class extends DefaultDeployer
{
    public function configure()
    {
        return $this->getConfigBuilder()
            // SSH connection string to connect to the remote server (format: user@host-or-IP:port-number)
            ->server('localhost')
            // the absolute path of the remote server directory where the project is deployed
            ->deployDir('/var/www/html/')
            // the URL of the Git repository where the project code is hosted
            ->repositoryUrl('ssh://gitlab@gitlab.cs.man.ac.uk:22222/m15806pt/bully-shield.git')
            // the repository branch to deploy
            ->repositoryBranch('deployment')
        ;
    }

    // run some local or remote commands before the deployment is started
    public function beforeStartingDeploy()
    {
        // $this->runLocal('./vendor/bin/simple-phpunit');
    }

    // run some local or remote commands after the deployment is finished
    public function beforeFinishingDeploy()
    {
        // $this->runRemote('{{ console_bin }} app:my-task-name');
        // $this->runLocal('say "The deployment has finished."');
    }
};