if [[ ${1}  = *"-rc."* ]]
then
  echo "reached in first if condition"
  curl https://downloads.traceable.ai/\#cli/rc/${{ inputs.cli_version }}/tars/traceable-cli-${{ inputs.cli_version }}-linux-x86_64.tar.gz -o ${GITHUB_WORKSPACE}/traceable-cli-${{ inputs.cli_version }}-linux-x86_64.tar.gz
  tar -xf ${GITHUB_WORKSPACE}/traceable-cli-${{ inputs.cli_version }}-linux-x86_64.tar.gz --directory ${GITHUB_WORKSPACE}
  echo "::set-env name=CLI_LOCATION::${GITHUB_WORKSPACE}/traceable-cli-${{ inputs.cli_version }}-linux-x86_64"
fi
if [[ ${1} = "latest" ]]
then
  ls -la
fi
echo "reached the end of run"