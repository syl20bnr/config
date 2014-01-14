function noproxy -d "Call a command without any proxy"
  begin; set -lx http_proxy; set -lx https_proxy;  set -lx HTTP_PROXY; set -lx HTTPS_PROXY; eval $argv; end
end