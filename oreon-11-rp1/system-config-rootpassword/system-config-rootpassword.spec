%global source0_hash 8d0b526c203525b7c2608b85b351b3a85f34088e03cfdaa2c29bc3e70944a37f
Name:           system-config-rootpassword
Version:        1.99.6
Release:        35%{?dist}
Summary:        A graphical interface for modifying the rootpassword
License:        GPL-1.0-or-later
URL:            http://fedora.redhat.com/
Source0:        %{name}-%{version}.tar.gz
Patch1:         system-config-rootpassword-python3.patch
Requires:       usermode >= 1.36
Requires:       libuser-python3 >= 0.49
Requires:       python3-pwquality
Requires:       python3-newt
Requires:       usermode-gtk
BuildArch:      noarch
Obsoletes:      redhat-config-rootpassword
Provides:       redhat-config-rootpassword = %{version}
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  make
# /oreon:deps
%description
A graphical user interface that allows the user to change the root password
of the system.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P1 -p1 -b .python3

%build

make %{?_smp_mflags}
%install
make INSTROOT=%{buildroot} install
desktop-file-install \
        --dir %{buildroot}%{_datadir}/applications   \
        %{buildroot}%{_datadir}/applications/system-config-rootpassword.desktop
%find_lang %{name}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
