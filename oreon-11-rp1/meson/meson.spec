%global source0_hash 09cc2faedc61262fc62abf57aa6c47c57a8c0730b950609a0711bbaf587bd133
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: meson
Version: 1.11.2
Release: 2%{?dist}
Summary: Build system
License: Apache-2.0
URL: https://mesonbuild.com/
Source0: https://github.com/mesonbuild/meson/archive/refs/tags/%{version}.tar.gz

BuildRequires: oreon-rpm-macros
%if %{without bootstrap} && !0%{?bootstrap}
BuildRequires: python3
%endif
Requires: python3
Requires: ninja-build

%description
meson is a build system.

%prep
%oreon_sha256
%autosetup -n meson-%{version} -p1

%build

%install
sitelib=$(python3 -c 'import sysconfig; print(sysconfig.get_path("purelib"))')
mkdir -p %{buildroot}$sitelib %{buildroot}%{_bindir}
cp -a mesonbuild %{buildroot}$sitelib/
find %{buildroot} -type f -exec grep -I -l -E '^#! */usr/bin/env python' {} + | while read -r f; do
  sed -i '1s|^#! */usr/bin/env python.*|#!/usr/bin/python3|' "$f"
done
cat > %{buildroot}%{_bindir}/meson << 'EOF'
#!/usr/bin/python3
import sys
from mesonbuild.mesonmain import main
sys.exit(main())
EOF
chmod 755 %{buildroot}%{_bindir}/meson
%oreon_filelist
while read -r f; do
  case "$f" in
    *.py) printf '%s\n' "$(dirname "$f")/__pycache__/*" ;;
  esac
done < %{_builddir}/%{name}.files | sort -u >> %{_builddir}/%{name}.files

%files -f %{_builddir}/%{name}.files
%license COPYING
