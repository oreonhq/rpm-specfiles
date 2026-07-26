%global source0_hash 11fb5e47ec8d445871e2972ffd7afc213a9c1892f772e1e06830ce430178581e

Name:             ddccontrol-db
URL:              https://github.com/ddccontrol/ddccontrol-db
Version:          20260120
Release:          1%{?dist}
# Agreed by usptream to be GPLv2+
# http://sourceforge.net/mailarchive/message.php?msg_id=29762202
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:          GPL-2.0-or-later
Summary:          DDC/CI control database for ddccontrol
Source0:          https://github.com/ddccontrol/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
# use autopoint instead of gettextize that is interactive tool
BuildRequires:    gettext
BuildRequires:    gettext-devel
BuildRequires:    libtool
BuildRequires:    intltool
BuildRequires:    perl(XML::Parser)
BuildRequires:    gcc
BuildRequires:    make
BuildArch:        noarch

%description
DDC/CU control database for DDCcontrol.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

./autogen.sh

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
%find_lang %{name}

%files -f %{name}.lang
%license COPYING
%doc AUTHORS NEWS README.md
%{_datadir}/%{name}

%changelog
%autochangelog
