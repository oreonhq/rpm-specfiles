%global source0_hash 77a8b7823cd09405a0eed92b99d4366431517f8ce0296032d6037eeaa223b92c

Name:           python-nbxmpp
Version:        4.5.4
Release:        7%{?dist}
Summary:        Python library for non-blocking use of Jabber/XMPP
# Automatically converted from old format: GPLv3 - review is highly recommended.
License:        GPL-3.0-only
URL:            https://dev.gajim.org/gajim/python-nbxmpp/
Source0:        https://dev.gajim.org/gajim/python-nbxmpp/-/archive/%{version}/python-nbxmpp-%{version}.tar.bz2

BuildArch:      noarch
BuildRequires:  python3-devel

%global desc %{expand:
python-nbxmpp is a Python library that provides a way for Python applications
to use Jabber/XMPP networks in a non-blocking way.}

%description
%{desc}

%package -n python3-nbxmpp
Summary:        %{summary}
Requires:       python3-gobject >= 3.42.0
Requires:       glib2 >= 2.66
Requires:       libsoup3
Recommends:     python3-gssapi
Obsoletes:      python-nbxmpp-doc < 1.0.0

%description -n python3-nbxmpp
%{desc}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files nbxmpp

%files -n python3-nbxmpp -f %{pyproject_files}
%doc README.md ChangeLog

%changelog
%autochangelog
