# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 64731a3a08ae94837e480f866cb1a2be9b12b9010899317f1db097ce5281a52a

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap
%global libname mesonbuild

%bcond check 1
%bcond docs 1

Name:           meson
Version:        1.12.1
Release:        1%{?dist}
Summary:        High productivity build system

License:        Apache-2.0
URL:            https://mesonbuild.com/
Source0:        https://github.com/mesonbuild/meson/archive/%{version}/meson-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pip
Requires:       ninja-build

Requires:       meson-srpm-macros = %{version}-%{release}

%if %{with docs}
BuildRequires:  python3-pyyaml
%endif
%if %{with check} || %{with docs}
BuildRequires:  ninja-build
%endif
%if %{with check}
# Some tests expect the unversioned executable
BuildRequires:  /usr/bin/python
# Various languages
BuildRequires:  gcc
BuildRequires:  libasan
BuildRequires:  gcc-c++
BuildRequires:  gcc-gfortran
BuildRequires:  gcc-objc
BuildRequires:  gcc-objc++
BuildRequires:  java-25-devel
BuildRequires:  libomp-devel
BuildRequires:  mono-core mono-devel
BuildRequires:  rust
# Since the build is noarch, we can't use %%ifarch
#%%ifarch %%{ldc_arches}
#BuildRequires:  ldc
#%%endif
# Various libs support
BuildRequires:  boost-devel
BuildRequires:  /usr/bin/clang-format
BuildRequires:  clippy
BuildRequires:  gtest-devel
BuildRequires:  gmock-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtbase-private-devel
BuildRequires:  qt5-linguist
BuildRequires:  vala
BuildRequires:  python3-gobject-base
BuildRequires:  wxGTK-devel
BuildRequires:  bindgen
BuildRequires:  flex
BuildRequires:  bison
BuildRequires:  gettext
BuildRequires:  gnustep-base-devel
BuildRequires:  /usr/bin/gnustep-config
BuildRequires:  git-core
BuildRequires:  pkgconfig(protobuf)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(glib-sharp-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  gtk-doc
BuildRequires:  itstool
BuildRequires:  mercurial
BuildRequires:  gcovr
BuildRequires:  pkgconfig(zlib)
BuildRequires:  python3dist(cython)
BuildRequires:  python3dist(fastjsonschema)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  /usr/bin/pcap-config
BuildRequires:  pkgconfig(vulkan)
BuildRequires:  llvm-devel
BuildRequires:  cups-devel
BuildRequires:  /usr/bin/wx-config
BuildRequires:  /usr/bin/sdl2-config
BuildRequires:  oreon-rpm-macros
%endif

# generated BuildRequires, refresh with: orbscli plan bake
BuildRequires: python3dist(setuptools) >= 42

%description
Meson is a build system designed to optimize programmer
productivity. It aims to do this by providing simple, out-of-the-box
support for modern software development tools and practices, such as
unit tests, coverage reports, Valgrind, CCache and the like.

%package srpm-macros
Summary:        rpm macros to build projects using meson
Conflicts:      meson < 1.12.0-2

%description srpm-macros
This package contains %{summary}.

%prep
%oreon_sha256

%autosetup -p1
# Macro should not change when we are redefining bindir
sed -i -e "/^%%__meson /s| .*$| %{_bindir}/%{name}|" data/macros.%{name}
# Automatically pull in meson if the build system is used
sed -i -e '/^%%buildsystem_meson_generate_buildrequires/s|%%{nil}|echo "meson"|' data/macros.%{name}

%build
%pyproject_wheel

%if %{with docs}
%{python3} ./meson.py setup docs docs.build \
	--prefix=%{_prefix} --mandir=%{_mandir} -Dhtml=false -Dunsafe_yaml=true
%{python3} ./meson.py compile -C docs.build
%endif

%install
%pyproject_install
%pyproject_save_files -l mesonbuild

%if %{with docs}
%{python3} ./meson.py install -C docs.build --destdir=%{buildroot}
%endif

install -Dpm0644 -t %{buildroot}%{rpmmacrodir} data/macros.%{name}
install -Dpm0644 -t %{buildroot}%{_datadir}/bash-completion/completions/ data/shell-completions/bash/meson
install -Dpm0644 -t %{buildroot}%{_datadir}/zsh/site-functions/ data/shell-completions/zsh/_meson

%if %{with check}
%check
export MESON_PRINT_TEST_OUTPUT=1
%{python3} ./run_unittests.py -v
%endif

%files -f %{pyproject_files}
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%if %{with docs}
%{_mandir}/man3/%{name}-reference.3*
%endif
%dir %{_datadir}/polkit-1
%dir %{_datadir}/polkit-1/actions
%{_datadir}/polkit-1/actions/com.mesonbuild.install.policy
%{_datadir}/bash-completion/completions/meson
%{_datadir}/zsh/site-functions/_meson

%files srpm-macros
%{rpmmacrodir}/macros.%{name}

