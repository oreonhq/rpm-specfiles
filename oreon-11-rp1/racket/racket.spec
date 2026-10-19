%global source0_hash 14f974b12c55357a20d187bce3137f999f001d011d81fcae0fdbb287dbfe5afd
%global _find_debuginfo_opts --keep-section .rackboot
Name:           racket
Version:        9.3
Release:        1%{?dist}
Summary:        General purpose programming language
License:        MIT AND Apache-2.0
URL:            https://racket-lang.org
Source0:        https://download.racket-lang.org/installers/%{version}/%{name}-%{version}-src.tgz
Patch0:         racket-configure-c99.patch
ExcludeArch:    ppc64le s390x
Requires:       racket-minimal%{?_isa} = %{version}-%{release}
Requires:       racket-pkgs = %{version}-%{release}
Recommends:     racket-doc = %{version}-%{release}
# oreon:deps
BuildRequires:  cairo
BuildRequires:  chrpath
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  git
BuildRequires:  glib2
BuildRequires:  gtk3
BuildRequires:  libffi-devel
BuildRequires:  libjpeg-turbo
BuildRequires:  libpng
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pango
# /oreon:deps
%description
Racket is a general-purpose programming language as well as
the world's first ecosystem for developing and deploying new
languages. Make your dream language, or use one of the dozens
already available.

# Equivalent to upstream's minimal-racket release
%package        minimal
Summary:        A minimal Racket installation
Requires:       racket-collects = %{version}-%{release}
%description    minimal
Racket's core runtime

%package        collects
Summary:        Racket's core collections libraries
BuildArch:      noarch
%description    collects
Libraries providing Racket's core functionality

# Arch independent source and bytecode files
%package        pkgs
Summary:        Racket package collections
Requires:       gtk3
Requires:       cairo
Requires:       pango
Requires:       libpng
Requires:       glib2
Requires:       libjpeg-turbo
Requires:       racket-minimal = %{version}-%{release}
BuildArch:      noarch
%description    pkgs
Additional packages and libraries for Racket

# Development headers and links
%package        devel
Summary:        Development files for Racket
Requires:       racket-minimal%{?_isa} = %{version}-%{release}
%description    devel
Files needed to link against Racket.

# HTML documentation
%package        doc
Summary:        Documentation files for Racket
BuildArch:      noarch
%description    doc
A local installation of the Racket documentation system.

%prep

%autosetup -p2

# Remove bundled libffi
rm -r src/bc/foreign/libffi

%build

cd src
%configure \
        --enable-pthread \
        --enable-shared \
        --enable-libffi \
        --disable-libs \
%ifarch ppc64le s390x
        --enable-pb \
%endif
%ifarch ppc64le
        --enable-mach=tpb64l \
%endif
%ifarch s390x
        --enable-mach=tpb64b \
%endif
        --enable-lt="%{_bindir}/libtool" \
        --disable-strip
%make_build
%install
%make_install -C src
rm %{buildroot}%{_bindir}/mred
rm %{buildroot}%{_bindir}/mred-text
ln -s gracket %{buildroot}%{_bindir}/mred
ln -s gracket-text %{buildroot}%{_bindir}/mred-text
chrpath --delete %{buildroot}%{_bindir}/racket
chrpath --delete %{buildroot}%{_libdir}/racket/gracket
sed -i "s#%{buildroot}##g" %{buildroot}/%{_datadir}/applications/*.desktop
desktop-file-validate %{buildroot}/%{_datadir}/applications/*.desktop
for i in $(find %{buildroot}/%{_datadir}/doc/racket/ -name '*.html'); do
  sed -i "s#%{buildroot}##g" $i
done
chmod -x %{buildroot}%{_libdir}/racket/starter-sh
%undefine __arch_install_post
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%{buildroot}%{_bindir}/%{name} --version
%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list
%files -n racket-minimal -f %{oreon_filedir}/racket-minimal.list
%files -n racket-collects -f %{oreon_filedir}/racket-collects.list
%files -n racket-pkgs -f %{oreon_filedir}/racket-pkgs.list
%files -n racket-devel -f %{oreon_filedir}/racket-devel.list
%files -n racket-doc -f %{oreon_filedir}/racket-doc.list

%changelog

%autochangelog
