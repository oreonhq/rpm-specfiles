%global source0_hash 3b45890fb3e3c2a1bdebb089d42897a9fd6d2ac18ceedafe77c1b1327244bb1f

%global commit0 627468b537befb16c0d04e426450b2fe7eb85c9f
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global date0   20170903

Name:           openconnect-gateway
Version:        0 
Release:        0.11.%{date0}git%{shortcommit0}%{?dist}
Summary:        Connect to a VPN without routing everything through the VPN

License:        MIT
URL:            https://github.com/millermatt/%{name}
Source0:        %{url}/archive/%{commit0}/%{name}-%{shortcommit0}.tar.gz

BuildArch:      noarch
Requires:       ca-certificates openconnect wget      

%description
%{summary}.
Some sample scripts to run in shell.
See readme.md for proper usage.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n%{name}-%{commit0}

%build
# no

%install
mkdir -p %{buildroot}/%{_bindir}
cp -av connect.sh %{buildroot}/%{_bindir}/%{name}

%files
%license LICENSE
%doc readme.md
%doc Vagrantfile
%doc *.sh
%{_bindir}/%{name}

%changelog
%autochangelog
