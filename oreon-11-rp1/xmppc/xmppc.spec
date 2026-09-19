%global source0_hash 05259ec5cba25f693edfe01389a3405835404539c7817fb208c201e29480e6b7

Name:           xmppc
Version:        0.1.2
Release:        11%{?dist}
Summary:        A command-line interface (CLI) XMPP Client

# Automatically converted from old format: GPLv3 - review is highly recommended.
License:        GPL-3.0-only
URL:            https://codeberg.org/Anoxinon_e.V./%{name}
Source0:        https://codeberg.org/Anoxinon_e.V./%{name}/archive/%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  automake
BuildRequires:  autoconf
BuildRequires:  libtool
BuildRequires:  libstrophe-devel
BuildRequires:  glib2-devel
BuildRequires:  gpgme-devel
# For docs:
BuildRequires:  doxygen
BuildRequires:  asciidoc

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

%autosetup -n %{name}

%build
autoreconf -i -W all
%configure
%make_build

# Build HTML documentation
pushd doc/
make  # results are in doc/doxygen/html/
popd

%install
%make_install
# Install HTML documentation for the doc subpackage
# (destination directory already exists)
cp -a doc/doxygen/html/ %{buildroot}%{_pkgdocdir}/

%check
make check

%files
%license LICENSE
%doc README.md changelog
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.*

%files doc
%{_pkgdocdir}/html/
%{_pkgdocdir}/%{name}.1.html

%changelog
%autochangelog
