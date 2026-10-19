%global source0_hash 05259ec5cba25f693edfe01389a3405835404539c7817fb208c201e29480e6b7
Name:           xmppc
Version:        0.1.2
Release:        1%{?dist}
Summary:        A command-line interface (CLI) XMPP Client
License:        GPL-3.0-only
URL:            https://codeberg.org/Anoxinon_e.V./%{name}
Source0:        https://codeberg.org/Anoxinon_e.V./%{name}/archive/%{version}.tar.gz
# oreon:deps
BuildRequires:  asciidoc
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  glib2-devel
BuildRequires:  gpgme-devel
BuildRequires:  libstrophe-devel
BuildRequires:  libtool
# /oreon:deps
%description
xmppc is a XMPP command line interface client. It's written in C and
is using the xmpp library libstrophe.

%package        doc
Summary:        Documentation for %{name}
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
%description    doc
The %{name}-doc package contains HTML documentation for developing
applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}
%oreon_prep
%build

autoreconf -i -W all
%configure
%make_build
pushd doc/
make  # results are in doc/doxygen/html/
popd
%install
%make_install
cp -a doc/doxygen/html/ %{buildroot}%{_pkgdocdir}/
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

make check
%files -f %{oreon_filedir}/main.list
%files -n xmppc-doc -f %{oreon_filedir}/xmppc-doc.list

%changelog

%autochangelog
