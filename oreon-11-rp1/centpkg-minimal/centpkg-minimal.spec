%global source0_hash 37845c5452df01ba34579063b37c97a85d91e3da7206636ea6e57fe1a3c5cdb8

Name:           centpkg-minimal
Version:        2.1.0
Release:        9%{?dist}
Summary:        Used by koji to download sources for building CentOS

License:        GPL-2.0-only
URL:            https://git.centos.org/centos-git-common
Source0:        %{name}.tar.gz
Source1:        centpkg

BuildArch:      noarch
Requires:       util-linux
Requires:       curl
Requires:       git-core
Conflicts:      centpkg

%description
Used by koji to download sources for building CentOS

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -c -n centpkg-minimal
cp %{SOURCE1} .

%build

%install
install -d %{buildroot}%{_bindir}
install -pm 755 get_sources.sh %{buildroot}%{_bindir}/get_sources.sh
install -pm 755 centpkg %{buildroot}%{_bindir}/centpkg

%files
%{_bindir}/get_sources.sh
%{_bindir}/centpkg

%changelog
%autochangelog
