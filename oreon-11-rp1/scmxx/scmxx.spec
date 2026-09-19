%global source0_hash 60bd84bd4b9c6b0d87be59e080b4776320d60aa025ed57560a5790b511d5d6da

Summary: Exchange data with Siemens mobile phones
Name: scmxx
Version: 0.9.0
Release: 36%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
URL: http://www.hendrik-sattler.de/scmxx
Source0: http://dl.sourceforge.net/scmxx/scmxx-%{version}.tar.bz2
Patch0: scmxx-configure-c99.patch
BuildRequires: make
BuildRequires:  gcc
BuildRequires: libxslt-devel, gettext

%description
SCMxx is a console program that allows you to exchange certain types of
data with mobile phones made by Siemens. Some of the data types that can be
exchanged are logos, ring tones, vCalendars, phonebook entries, and short
messages. Other actions like setting the time and dialling a number are also
possible.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%configure \
	--with-device=/dev/ttyS0 \
	--with-baudrate=115200
%{__make}

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS BUGS LICENSE CHANGELOG README docs/gsmcharset.txt
%{_bindir}/adr2vcf
%{_bindir}/apoconv
%{_bindir}/scmxx
%{_bindir}/smi
%{_mandir}/man1/scmxx.1.gz
%lang(de) %{_mandir}/de/man1/scmxx.1.gz
%lang(it) %{_mandir}/it/man1/scmxx.1.gz
%lang(ru) %{_mandir}/ru/man1/scmxx.1.gz

%changelog
%autochangelog
