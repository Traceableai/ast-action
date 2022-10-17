ls -la
if [[ ${1}  = *"-rc."* ]]
then
  curl -OL https://downloads.traceable.ai/cli/rc/${1}/tars/traceable-cli-${1}-linux-x86_64.tar.gz
fi
if [[ ${1} = "latest" ]]
then
  curl -OL https://downloads.traceable.ai/cli/rc/${1}/traceable-cli-${1}-linux-x86_64.tar.gz
fi
tar -xvf ${GITHUB_WORKSPACE}/traceable-cli-${1}-linux-x86_64.tar.gz --directory ${GITHUB_WORKSPACE}