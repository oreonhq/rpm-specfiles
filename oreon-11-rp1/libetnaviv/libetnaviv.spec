%global source0_hash cc234638dffb3faf2696f8b5fb91a157416674c86fb2701800dac55f502ffabd

%global commit 60105d1b0755e48b37d779d8a2b9c4b458b5a2fd
%global shortcommit %(c=%{commit}; echo ${c:0:7})

# We don't build any binaries.
%undefine _debugsource_packages

Name:           libetnaviv
Version:        1.0.0
Release:        16.20141102git%{shortcommit}%{?dist}
Summary:        Vivante GPU user-space driver

License:        MIT
URL:            https://github.com/etnaviv/libetnaviv.git
Source0:        https://github.com/etnaviv/%{name}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
# https://github.com/etnaviv/libetnaviv/pull/2
Patch0:         https://github.com/lkundrak/libetnaviv/commit/e61d9e169.patch#/0001-etna.h-include-other-headers-from-the-same-directory.patch

%description
Project Etnaviv is an open source user-space driver for the Vivante GCxxx
series of embedded GPUs.

%package -n etnaviv-headers
Summary:        Header files for etnaviv.
BuildArch:      noarch

%description -n etnaviv-headers
Header files for etnaviv.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{commit}
%patch -P0 -p1

%build
# We don't actually build libetnaviv. It would only work with the out-of-tree
# galcore kernel module and needs its headers to build anyway.
# We just need the headers.

%install
mkdir -p %{buildroot}%{_includedir}/etnaviv/
install -pm644 src/*.h %{buildroot}%{_includedir}/etnaviv/

%files -n etnaviv-headers
%{_includedir}/etnaviv
%doc README.md

%changelog
%autochangelog
