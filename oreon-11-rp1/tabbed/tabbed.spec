%global source0_hash 6e8682230a213d7dabf8a79306bd3ce023875b2295a9097db427d65c1c68f322

# XXX: Drop once f36 goes EOL
%if 0%{?fedora} == 036
%undefine _package_note_file
%endif

Name:           tabbed
Version:        0.7
Release:        8%{?dist}
Summary:        Simple Xembed container manager

%global         _tabbedsourcedir %{_usrsrc}/tabbed-user-%{version}-%{release}

License:        MIT
URL:            http://tools.suckless.org/tabbed
Source0:        http://dl.suckless.org/tools/%{name}-%{version}.tar.gz
Source1:        %{name}-user
Source2:        %{name}-user.1
# Upstream tarball doesn't include the xembed manpage in 0.6; taken from
# the git repository (fixed in 910e67db).
Source3:        xembed.1
BuildRequires:  binutils
BuildRequires:  coreutils
BuildRequires:  fontconfig-devel
BuildRequires:  gcc
BuildRequires:  libX11-devel
BuildRequires:  libXft-devel
BuildRequires:  make
BuildRequires:  sed
Requires(post): %{_sbindir}/update-alternatives
Requires(postun): %{_sbindir}/update-alternatives

%description
A simple generic fronted to XEmbed aware applications.

%package user
Summary:        Tabbed sources and tools for user configuration
License:        MIT
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       binutils
Requires:       coreutils
Requires:       findutils
Requires:       fontconfig-devel
Requires:       gcc
Requires:       libX11-devel
Requires:       libXft-devel
Requires:       make
Requires:       patch
Requires:       redhat-rpm-config
Requires:       sed
Requires(post): %{_sbindir}/update-alternatives
Requires(postun): %{_sbindir}/update-alternatives

%description user
Tabbed source files and a launcher/builder wrapper script for
customized configurations.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
# XXX: To be dropped with 0.8+
cp %{SOURCE3} .
sed -e 's|/usr/local|%{_prefix}|g' \
    -e 's|/usr/lib|%{_libdir}|g' \
    -e 's|-std=c99 -pedantic -Wall -Os|%{optflags}|g' \
    -e 's|-s\b||' \
    -e 's|\(${LIBS}\)|\1 %{?__global_ldflags}|' \
    -i config.mk
sed -i 's!^\(\t\+\)@!\1!' Makefile 

%build
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
mv %{buildroot}%{_bindir}/%{name}{,-fedora}
install -pm755 %{SOURCE1} %{buildroot}%{_bindir}/%{name}-user
install -Dpm644 %{SOURCE2} %{buildroot}%{_mandir}/man1/%{name}-user.1
for file in \
    %{buildroot}%{_bindir}/%{name}-user \
    %{buildroot}%{_mandir}/man1/%{name}-user.1; do
sed -i -e 's/VERSION/%{version}/' \
       -e 's/RELEASE/%{release}/' \
       ${file}
done
mkdir -p %{buildroot}%{_tabbedsourcedir}
install -m644 arg.h config.def.h config.mk Makefile tabbed.c xembed.c \
     %{buildroot}%{_tabbedsourcedir}
touch %{buildroot}%{_bindir}/%{name}

%pre
[ -L %{_bindir}/%{name} ] || rm -f %{_bindir}/%{name}

%post
%{_sbindir}/update-alternatives --install %{_bindir}/%{name} %{name} \
    %{_bindir}/%{name}-fedora 10

%postun
if [ $1 -eq 0 ] ; then
    %{_sbindir}/update-alternatives --remove %{name} %{_bindir}/%{name}-fedora
fi

%post user
%{_sbindir}/update-alternatives --install %{_bindir}/%{name} %{name} \
    %{_bindir}/%{name}-user 20

%postun user
if [ $1 -eq 0 ] ; then
    %{_sbindir}/update-alternatives --remove %{name} %{_bindir}/%{name}-user
fi

%files
%doc LICENSE README
%ghost %{_bindir}/%{name}
%{_bindir}/%{name}-fedora
%{_bindir}/xembed
%{_mandir}/man1/%{name}.*
%{_mandir}/man1/xembed.*

%files user
%ghost %{_bindir}/%{name}
%{_bindir}/%{name}-user
%{_mandir}/man1/%{name}-user.*
%{_tabbedsourcedir}

%changelog
%autochangelog
