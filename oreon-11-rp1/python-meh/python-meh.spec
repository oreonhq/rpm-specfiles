%global source0_hash 7b66046b4693e7631aad299e5a55d0255962608cd03372f559745c575aa8c920

%global libreportver 2.0.18-1

Summary:  A python library for handling exceptions
Name: python-meh
Url: https://github.com/rhinstaller/python-meh
Version: 0.52
Release: 12%{?dist}
# This is a Red Hat maintained package which is specific to
# our distribution.  Thus the source is only available from
# within this srpm.
# This tarball was created from upstream git:
#   git clone https://github.com/rhinstaller/python-meh
#   cd python-meh && make archive
Source0:        https://github.com/rhinstaller/python-meh/archive/%{name}-%{version}.tar.gz

License: GPL-2.0-or-later
BuildArch: noarch
BuildRequires: make
BuildRequires: gettext
BuildRequires: intltool
%if 0%{?rhel} < 10 || 0%{?fedora}
BuildRequires: libreport-gtk >= %{libreportver}
BuildRequires: libreport-cli >= %{libreportver}
BuildRequires: python3-libreport >= %{libreportver}
%endif
BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: python3-dbus

%global _description\
The python-meh package is a python library for handling, saving, and reporting \
exceptions.

%description %_description

%package -n python3-meh
Summary:  A python 3 library for handling exceptions
%{?python_provide:%python_provide python3-meh}
Obsoletes: python-meh < 0.46-1
Obsoletes: python2-meh < 0.46-1
Requires: python3
Requires: python3-dbus
Requires: python3-rpm
%if 0%{?rhel} < 10 || 0%{?fedora}
Requires: libreport-cli >= %{libreportver}
Requires: python3-libreport >= %{libreportver}
%endif

%description -n python3-meh
The python3-meh package is a python 3 library for handling, saving, and reporting
exceptions.

%package -n python3-meh-gui
Summary: Graphical user interface for the python3-meh library
%{?python_provide:%python_provide python3-meh-gui}
Obsoletes: python-meh-gui < 0.46-1
Obsoletes: python2-meh-gui < 0.46-1
Requires: python3-meh = %{version}-%{release}
Requires: python3-gobject, gtk3
%if 0%{?rhel} < 10 || 0%{?fedora}
Requires: libreport-gtk >= %{libreportver}
%endif

%description -n python3-meh-gui
The python3-meh-gui package provides a GUI for the python3-meh library.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n %{name}-%{name}-%{version}

%build
make

%check
make test

%install
make DESTDIR=%{buildroot} install

# Upstream ships no installed gettext catalogs in the release tarball (empty po
# tree in practice), so %%find_lang would always fail with "No translations found".

%files -n python3-meh
%doc COPYING
%{python3_sitelib}/*
%exclude %{python3_sitelib}/meh/ui/gui.py*
%exclude %{python3_sitelib}/meh/ui/__pycache__/gui.*

%files -n python3-meh-gui
%{python3_sitelib}/meh/ui/gui.py*
%{python3_sitelib}/meh/ui/__pycache__/gui.*
%{_datadir}/python-meh

%changelog
* Sun Apr 19 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.52-11
- Drop %%find_lang when no catalogs are installed (find-lang.sh exits 1)

* Sat Apr 18 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.52-10
- Fix prep section directory name for GitHub archive

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.52-9
- Prepare for Oreon 11 (RP1)
