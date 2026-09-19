%global source0_hash 65e91607643e5aa5b336f17636fa474eb6669acc89288e72feb2f54a27edb88e

Name:            cronolog
Version:         1.6.2
Release:         46%{?dist}
Summary:         Web log rotation program for Apache

License:         Apache-1.0
URL:             http://cronolog.org/
Source0:         http://cronolog.org/download/%{name}-%{version}.tar.gz
BuildRequires:  gcc
Patch1:          cronolog-largefile.patch
Patch2:          cronolog-configure-c99.patch
Patch3:          cronolog-c99.patch
Patch4:          cronolog-gcc15.patch
BuildRequires:          perl-generators
BuildRequires: make

%description
cronolog is a simple filter program that reads log file entries from
standard input and writes each entry to the output file specified
by a filename template and the current date and time. When the
expanded filename changes, the current file is closed and a new one
opened. cronolog is intended to be used in conjunction with a Web server,
such as Apache, to split the access log into daily or monthly logs.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P1
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p1

%build
%configure
%make_build

%install
%make_install
sed -i 's|/www/sbin|/usr/sbin|g' %{buildroot}/%{_mandir}/man1/*
mkdir -p %{buildroot}/%{_bindir}
if [ "%{_sbindir}" != "%{_bindir}" ]; then
mv %{buildroot}/%{_sbindir}/cronosplit %{buildroot}/%{_bindir}
fi
rm -f %{buildroot}%{_infodir}/dir

%files
%doc AUTHORS COPYING ChangeLog NEWS README TODO
%{_sbindir}/*
%{_bindir}/*
%{_mandir}/man1/*
%{_infodir}/*

%changelog
%autochangelog
