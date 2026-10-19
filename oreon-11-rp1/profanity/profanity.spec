%global source0_hash c1e28a849aa178fd1ec5f384b0f8bdd244bce453dc4ef7bb76d0830382fec304
Name:           profanity
Version:        0.18.2
Release:        1%{?dist}
Summary:        A console based XMPP client
License:        GPL-3.0-only
URL:            https://profanity-im.github.io/
Source0:        https://profanity-im.github.io/tarballs/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  autoconf-archive
BuildRequires:  automake
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  glib2-devel
BuildRequires:  gpgme-devel
BuildRequires:  libcmocka-devel
BuildRequires:  libcurl-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  libnotify-devel
BuildRequires:  libotr-devel
BuildRequires:  libsignal-protocol-c-devel
BuildRequires:  libstrophe-devel
BuildRequires:  libtool
BuildRequires:  ncurses-devel
BuildRequires:  python-unversioned-command
BuildRequires:  python3-devel
BuildRequires:  python3dist(docutils)
BuildRequires:  python3dist(sphinx)
BuildRequires:  qrencode-devel
BuildRequires:  readline-devel
BuildRequires:  sqlite-devel
BuildRequires:  texinfo
BuildRequires:  tree
# /oreon:deps
%description
Profanity is a console based XMPP client written in C using ncurses
and libstrophe, inspired by Irssi.

%package libs
Summary:       The shared libraries required for plugins of Profanity
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description libs
The %{name}-libs package provides the essential shared libraries for any
plugin of Profanity written in C.

See: https://profanity-im.github.io/plugins.html

%package        devel
Summary:        Development files for libraries used by plugins of Profanity
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing plugins written in C for Profanity.

%package        doc
Summary:        Documentation for %{name}
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
%description    doc
The %{name}-doc package contains docbook documentation for developing
applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup
# Output docbook instead of HTML
sed -i "s/GENERATE_HTML          = YES/GENERATE_HTML          = NO/g" apidocs/c/c-prof.conf
sed -i "s/GENERATE_DOCBOOK       = NO/GENERATE_DOCBOOK       = YES/g" apidocs/c/c-prof.conf
sed -i "s/DOCBOOK_PROGRAMLISTING = NO/DOCBOOK_PROGRAMLISTING = YES/g" apidocs/c/c-prof.conf

%build

autoreconf -i -W all
%configure
%make_build
pushd apidocs/c/
doxygen c-prof.conf  # results are in apidocs/c/docbook/
tree
popd
pushd apidocs/python/
sphinx-apidoc -f -o . src
make texinfo  # results are in apidocs/python/_build/texinfo
pushd _build
pushd texinfo
makeinfo --docbook ProfanityPythonPluginsAPI.texi
tree
popd
popd
popd
%install
%make_install
rm -f %{buildroot}%{_libdir}/libprofanity.la
mkdir -p %{buildroot}%{_datadir}/help/en/profanity/
for file in apidocs/c/docbook/*.xml;
do
  install -m644 ${file} \
    %{buildroot}%{_datadir}/help/en/profanity
done
install -m644 apidocs/python/_build/texinfo/ProfanityPythonPluginsAPI.xml \
  %{buildroot}%{_datadir}/help/en/profanity
cp -a profrc.example %{buildroot}%{_datadir}/%{name}/
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

make check
%files -f %{oreon_filedir}/main.list
%files -n profanity-libs -f %{oreon_filedir}/profanity-libs.list
%files -n profanity-devel -f %{oreon_filedir}/profanity-devel.list
%files -n profanity-doc -f %{oreon_filedir}/profanity-doc.list

%changelog

%autochangelog
