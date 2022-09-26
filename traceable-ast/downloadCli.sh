if [[ ${1}  = *"-rc."* ]]
then
  curl -OL https://downloads.traceable.ai/cli/rc/${1}/tars/traceable-cli-${1}-linux-x86_64.tar.gz
  tar -xvf ${GITHUB_WORKSPACE}/traceable-cli-${1}-linux-x86_64.tar.gz --directory ${GITHUB_WORKSPACE}
  echo "CLI_LOCATION=${GITHUB_WORKSPACE}/traceable-cli-${1}-linux-x86_64" >> $GITHUB_ENV
fi
if [[ ${1} = "latest" ]]
then
  ls -la
fi
source ~/.bashrc
