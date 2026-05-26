Name:           perftest
Summary:        IB Performance Tests
# Upstream uses a dash in the version. Not valid in the Version field, so we use a dot instead.
# Issue "Please avoid dashes in version":
#   https://github.com/linux-rdma/perftest/issues/18
%global upstream_ver 25.10.0-0.128
Version:        %{gsub %upstream_ver - .}
Release:        %autorelease
License:        GPL-2.0-only OR BSD-2-Clause
Source:		https://github.com/linux-rdma/perftest/releases/download/25.10.0-0.128/perftest-25.10.0-0.128.gd01b183.tar.gz
Url:            https://github.com/linux-rdma/perftest
Patch0:		Perftest-Fix-RDMA-CM-DMAH-bug.patch
# oreon url source checksums begin
%global source0_sha256 750bc48b1d9362996de1d2bbe36d3b25f067b5077177d39c2faeb472bd5a7194
%global source0_file perftest-25.10.0-0.128.gd01b183.tar.gz
# oreon url source checksums end

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  libibverbs-devel >= 1.2.0
BuildRequires:  librdmacm-devel >= 1.0.21
BuildRequires:  libibumad-devel >= 1.3.10.2
BuildRequires:  pciutils-devel
Obsoletes:      openib-perftest < 1.3
ExcludeArch:    s390 %{arm}

%description
Perftest is a collection of simple test programs designed to utilize 
RDMA communications and provide performance numbers over those RDMA
connections.  It does not work on normal TCP/IP networks, only on
RDMA networks.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/perftest-25.10.0-0.128.gd01b183.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "750bc48b1d9362996de1d2bbe36d3b25f067b5077177d39c2faeb472bd5a7194" || { echo "oreon: Source0 SHA256 mismatch for perftest-25.10.0-0.128.gd01b183.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
# The directory in the tarball has only the part before the dash.
%global tarball_ver %{lua: _,_,v=string.find(rpm.expand("%{upstream_ver}"),"([^-]+)"); print(v)}

%setup -q -n %{name}-%{tarball_ver}
find src -type f -iname '*.[ch]' -exec chmod a-x '{}' ';'
%autopatch -p1

%build
%configure
%make_build

%install
for file in ib_{atomic,read,send,write}_{lat,bw} raw_ethernet_{lat,bw}; do
	install -D -m 0755 $file %{buildroot}%{_bindir}/$file
done

%files
%doc README
%license COPYING
%_bindir/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - %{gsub%upstream_ver-.}-1
- Prepare for Oreon 11 (RP1)
