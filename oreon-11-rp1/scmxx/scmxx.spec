%global source0_hash 60bd84bd4b9c6b0d87be59e080b4776320d60aa025ed57560a5790b511d5d6da
Summary:        Exchange data with Siemens mobile phones
Name: scmxx
Version: 0.9.0
Release:        1%{?dist}
License: GPL-2.0-or-later
URL: http://www.hendrik-sattler.de/scmxx
Source0:        http://dl.sourceforge.net/scmxx/scmxx-%{version}.tar.bz2
Patch0: scmxx-configure-c99.patch
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  libxslt-devel
BuildRequires:  make
# /oreon:deps
%description
SCMxx is a console program that allows you to exchange certain types of
data with mobile phones made by Siemens. Some of the data types that can be
exchanged are logos, ring tones, vCalendars, phonebook entries, and short
messages. Other actions like setting the time and dialling a number are also
possible.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure \
	--with-device=/dev/ttyS0 \
	--with-baudrate=115200
%{__make}
%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
%find_lang %{name}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
