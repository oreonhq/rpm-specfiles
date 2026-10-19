%global source0004_hash 6fc9e709ccbfe0d77fbffa2427a983282be2eb88e47b1cdb49f21a83b4d1e665
%global source0_hash e30f52a9b449560f9a6748933cf1c7a21e8c08f630394655bf3f7d09246932a4
%define __spec_install_post                      \
%{?__debug_package:%{__debug_install_post}}      \
%{__arch_install_post}                           \
%{__os_install_post}                             \
fipshmac %{buildroot}%{_bindir}/%{newname}          \\\
  %{buildroot}%{_libexecdir}/%{newname}             \\\
  %{buildroot}%{_datadir}/%{newname}/openssl.cnf    \
c="%{buildroot}%{_datadir}/%{newname}/config.json"  \
if [[ -f ${c} ]]; then                           \
  fipshmac ${c}                                  \
fi                                               \
%{nil}
%{?__cmake_in_source_build:%undefine __cmake_in_source_build}
%global build_cflags   %(echo '%{build_cflags}'   | sed -e 's!-ffat-lto-objects!-fno-fat-lto-objects!g')
%global build_cxxflags %(echo '%{build_cxxflags}' | sed -e 's!-ffat-lto-objects!-fno-fat-lto-objects!g')
%global build_fflags   %(echo '%{build_fflags}' | sed -e 's!-ffat-lto-objects!-fno-fat-lto-objects!g')
%global build_fcflags  %(echo '%{build_fflags}' | sed -e 's!-ffat-lto-objects!-fno-fat-lto-objects!g')
%global qt6_build 0
%global pkg_sum   Online identification with German ID card (Personalausweis)
%global newname   AusweisApp
Name:             AusweisApp2
Version:          2.5.5
Release:        1%{?dist}
Summary:        Online identification with German ID card (Personalausweis)
License:          EUPL-1.2
URL:              https://www.ausweisapp.bund.de/en
%global rel_url   https://github.com/Governikus/%{name}/releases/download/%{version}
Source0000:       %{rel_url}/%{newname}-%{version}.tar.gz
Source0001:       %{rel_url}/%{newname}-%{version}.tar.gz.asc
Source0002:       %{name}-pubring.gpg
Source0003:       %{rel_url}/%{newname}-%{version}.tar.gz.sha256
Source0004:       https://joinup.ec.europa.eu/sites/default/files/custom-page/attachment/2020-03/EUPL-1.2%%20EN.txt#/EUPL-12_EN.txt
Source1000:       gen_openssl_cnf.py
Patch01000:       %{name}-1.24.1-use_Qt_TranslationsPath.patch
Patch01001:       0001-Use-legacy-OpenSSL-API.patch
%if 0%{?qt6_build}
%else
%endif
%global lc_name   %{lua:print(string.lower(rpm.expand("%{name}")))}
Obsoletes:        %{name}                < 1.20.1
Obsoletes:        %{lc_name}             < 1.20.1
Provides:         %{lc_name}             = %{version}-%{release}
Provides:         %{lc_name}%{?_isa}     = %{version}-%{release}
Requires:         %{name}-data           = %{version}-%{release}
Requires:         (%{name}-doc           = %{version}-%{release} if %{name}-doc)
%if !0%{?qt6_build}
Requires:         qt5-qtquickcontrols2%{?_isa}
%endif
Requires:         openssl-libs%{?_isa}  >= 3.0.8-2
%if 0%{?qt6_build}
Requires:         qt6-qtimageformats%{?_isa}
Requires:         qt6-qtsvg%{?_isa}
%endif
# oreon:deps
BuildRequires:  /usr/bin/fipshmac
BuildRequires:  /usr/bin/sha256sum
BuildRequires:  cmake
BuildRequires:  crypto-policies
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  gnupg2
BuildRequires:  hardlink
BuildRequires:  http-parser-devel
BuildRequires:  libappstream-glib
BuildRequires:  libudev-devel
BuildRequires:  libxkbcommon-devel
BuildRequires:  ninja-build
BuildRequires:  openssl-devel
BuildRequires:  pcsc-lite-devel
BuildRequires:  python3-devel
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx_rtd_theme
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  qt6-qtscxml-devel
BuildRequires:  qt6-qtshadertools-devel
BuildRequires:  qt6-qtsvg-devel
BuildRequires:  qt6-qttools-devel
BuildRequires:  qt6-qtwebsockets-devel
# /oreon:deps
%description
The AusweisApp2 is a software to identify yourself online
with your ID card (Personalausweis) or your electronic
residence permit (Aufenthalts- / Niederlassungserlaubis).

The AusweisApp2 also offers you an integrated self-assessment
in which you are able to view your data that is stored on the
online ID.

%package data
Summary:          Architecture-independent files used by %{name}
BuildArch:        noarch
Requires:         %{name}                = %{version}-%{release}
Requires:         hicolor-icon-theme
%description data
This package contains the architecture-independent files
used by %{name}.

%package doc
Summary:          User and API documentation for %{name}
BuildArch:        noarch
BuildRequires:    hardlink
BuildRequires:    python3-sphinx
BuildRequires:    python3-sphinx_rtd_theme
Requires:         (%{name}               = %{version}-%{release} if %{name})
%description doc
This package contains the user and API documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

# Verify tarball integrity.
%{gpgverify}                \
  --keyring='%{SOURCE2}'    \
  --signature='%{SOURCE1}'  \
  --data='%{SOURCE0}'
pushd %{_sourcedir}
sha256sum -c %{SOURCE3}
popd

%autosetup -p 1 -n %{newname}-%{version}
install -pm 0644 %{SOURCE4} LICENSE.en.txt

# Generate application specific OpenSSL configuration.
# See the comments in the resulting file for further information.
%{__python3} %{SOURCE1000} resources/config.json.in \
  > fedora_%{name}_openssl.cnf

# Create the shell wrapper.
cat << EOF > fedora_%{name}_wrapper.sh
#!/bin/sh
# /usr/bin/fipscheck                               \\
#     %{_bindir}/%{newname}                         \\
#     %{_libexecdir}/%{newname}                     \\
#     %{_datadir}/%{newname}/config.json           \\
#     %{_datadir}/%{newname}/openssl.cnf           \\
# || exit \$?;
OPENSSL_CONF=%{_datadir}/%{newname}/openssl.cnf  \\
%{_libexecdir}/%{newname} "\$@";
EOF

%build

%cmake                                     \
  -DBUILD_SHARED_LIBS:BOOL=OFF             \
  -DBUILD_TESTING:BOOL=OFF                 \
  -DCMAKE_BUILD_TYPE:STRING=Release        \
  -DINTEGRATED_SDK:BOOL=OFF                \
  -DPYTHON_EXECUTABLE:STRING=%{__python3}  \
  -DSELFPACKER:BOOL=OFF                    \
  -DUSE_SMARTEID:BOOL=ON                   \
  -G Ninja
%cmake_build
%ninja_build -C %{_vpath_builddir} installation_integration_de installation_integration_en notes sdk
%install
%cmake_install
mkdir -p %{buildroot}{%{_libexecdir},%{_qt5_translationdir}}
mv %{buildroot}%{_bindir}/%{newname} %{buildroot}%{_libexecdir}/%{newname}
install -pm 0755 fedora_%{name}_wrapper.sh %{buildroot}%{_bindir}/%{newname}
install -pm 0644 fedora_%{name}_openssl.cnf   \
  %{buildroot}%{_datadir}/%{newname}/openssl.cnf
%if !(0%{?qt6_build})
mv %{buildroot}%{_datadir}/%{newname}/translations/* \
  %{buildroot}%{_qt5_translationdir}
rm -fr %{buildroot}%{_datadir}/%{newname}/translations
%endif
mkdir -p %{buildroot}%{_pkgdocdir}/{installation_integration_{de,en},notes,sdk}
install -pm 0644 README.rst %{buildroot}%{_pkgdocdir}
cp -a %{_vpath_builddir}/docs/installation_integration_de/html/* %{buildroot}%{_pkgdocdir}/installation_integration_de
cp -a %{_vpath_builddir}/docs/installation_integration_en/html/* %{buildroot}%{_pkgdocdir}/installation_integration_en
cp -a %{_vpath_builddir}/docs/notes/html/* %{buildroot}%{_pkgdocdir}/notes
cp -a %{_vpath_builddir}/docs/sdk/html/* %{buildroot}%{_pkgdocdir}/sdk
find %{buildroot}%{_pkgdocdir} -type d -print0 | xargs -0 chmod -c 0755
find %{buildroot}%{_pkgdocdir} -type f -print0 | xargs -0 chmod -c 0644
find %{buildroot}%{_pkgdocdir} -type f -name '.*' -delete -print
hardlink -cfv %{buildroot}%{_pkgdocdir}
find %{buildroot}%{_datadir}/icons/hicolor -type f -print | \
sed -e 's!^%{buildroot}!!g' > %{lc_name}.icons
%if !(0%{?qt6_build})
%find_lang %{lc_name} --with-qt
%oreon_autofiles AusweisApp2-data usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles AusweisApp2-doc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%endif
%check

%ctest
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
%files -f %{oreon_filedir}/main.list
%files -n AusweisApp2-data -f %{oreon_filedir}/AusweisApp2-data.list
%files -n AusweisApp2-doc -f %{oreon_filedir}/AusweisApp2-doc.list

%changelog

%autochangelog
