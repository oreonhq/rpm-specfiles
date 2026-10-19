%global source0_hash e313c0602f980e2f77dd1399d09915a1c4ca28a82a7ff134c2e3108c3685878f
%global __cmake_in_source_build 1
%global snapdate 20140114
%global snaphash 35d9080f1870d44c384da8f17a46388ba97b9647
Name:           krazy2
Version:        2.97
Release:        1%{?dist}
Summary:        Krazy is a tool for checking code against the KDE coding guidelines
License:        GPL-2.0-or-later
URL:            http://techbase.kde.org/Development/Tutorials/Code_Checking
Source0:        https://gitorious.org/krazy/krazy/archive/%{snaphash}.tar.gz
Source1:        krazy-licensecheck
Patch0:         krazy2-install-shlibs.patch
Conflicts:      kdesdk < 4.2.0
Requires:       desktop-file-utils
# oreon:deps
BuildRequires:  cmake
BuildRequires:  groff
BuildRequires:  make
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(HTML::Parser)
BuildRequires:  perl(Pod::Perldoc)
BuildRequires:  perl(Tie::IxHash)
BuildRequires:  perl(XML::LibXML)
BuildRequires:  perl(YAML)
BuildRequires:  perl-generators
BuildRequires:  qt4-devel
# /oreon:deps
%description
Krazy scans KDE source code looking for issues that should be fixed
for reasons of policy, good coding practice, optimization, or any other
good reason.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n krazy-krazy
%patch -P0 -p1 -b .install-shlibs
# delete (two!) bundled copies of desktop-file-utils
rm -rf src/desktop-file-utils-*

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor
make
pushd src/passbyvalue
%{qmake_qt4}
make %{?_smp_mflags}
popd
pushd cppchecks
%{cmake} .
make %{?_smp_mflags} VERBOSE=1
popd
%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} PREFIX=%{_prefix} install
chmod 0755 %{buildroot}%{_bindir}/krazy2{,all,xml}
pushd helpers
make DESTDIR=%{buildroot} PREFIX=%{_prefix} \
    %if "%{_lib}" == "lib64"
        LIBSUFFIX=64 \
    %endif
    install
popd
pushd plugins
make PREFIX=%{buildroot}%{_prefix} \
    %if "%{_lib}" == "lib64"
        LIBSUFFIX=64 \
    %endif
    install
popd
pushd extras
make DESTDIR=%{buildroot} PREFIX=%{_prefix} \
    %if "%{_lib}" == "lib64"
        LIBSUFFIX=64 \
    %endif
    install
popd
pushd sets
make DESTDIR=%{buildroot} PREFIX=%{_prefix} \
    %if "%{_lib}" == "lib64"
        LIBSUFFIX=64 \
    %endif
    install
popd
pushd src/passbyvalue
make INSTALL_ROOT=%{buildroot}%{_prefix} \
    %if "%{_lib}" == "lib64"
        LIBSUFFIX=64 \
    %endif
    install
popd
pushd share
mkdir -p %{buildroot}%{_datadir}/dtd
install -m 644 -p kpartgui.dtd %{buildroot}%{_datadir}/dtd/kpartgui.dtd
install -m 644 -p kcfg.dtd %{buildroot}%{_datadir}/dtd/kcfg.dtd
popd
install -m 755 %{SOURCE1} %{buildroot}%{_bindir}/krazy-licensecheck
pushd cppchecks
make DESTDIR=%{buildroot} PREFIX=%{_prefix} install/fast
popd
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -type f -name perllocal.pod -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
%ldconfig_scriptlets
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
