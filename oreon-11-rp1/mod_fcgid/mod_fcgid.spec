Name:		mod_fcgid
Version:	2.3.9
Release:	37%{?dist}
Summary:	FastCGI interface module for Apache 2
License:	Apache-2.0
URL:		http://httpd.apache.org/mod_fcgid/
Source0:	http://www.apache.org/dist/httpd/mod_fcgid/mod_fcgid-%{version}.tar.bz2
Source2:	mod_fcgid-2.1-README.RPM
Source3:	mod_fcgid-2.1-README.SELinux
Source4:	mod_fcgid-tmpfs.conf
Source5:	fcgid24.conf
Patch0:		mod_fcgid-2.3.4-fixconf-shellbang.patch
Patch1:		mod_fcgid-2.3.9-segfault-upload.patch
Patch2:		mod_fcgid-2.3.9-r1848298.patch
BuildRequires:	coreutils
BuildRequires:	gcc
BuildRequires:	httpd-devel >= 2.4
BuildRequires:	make
BuildRequires:	pkgconfig
BuildRequires:	sed
# systemd-rpm-macros needed for definition of %%{_tmpfilesdir}
%if (0%{?fedora} && 0%{?fedora} <= 30) || 0%{?oreon}
BuildRequires:	systemd
%else
BuildRequires:	systemd-rpm-macros
%endif
Requires:	httpd-mmn = %{_httpd_mmn}
# systemd needed for ownership of %%{_tmpfilesdir}
Requires:	systemd

%description
mod_fcgid is a binary-compatible alternative to the Apache module mod_fastcgi.
mod_fcgid has a new process management strategy, which concentrates on reducing
the number of fastcgi servers, and kicking out corrupt fastcgi servers as soon
as possible.

%prep
%setup -q
cp -p %{SOURCE2} README.RPM
cp -p %{SOURCE3} README.SELinux
cp -p %{SOURCE5} fcgid24.conf

# Fix shellbang in fixconf script for our location of sed
%if (0%{?rhel} && 0%{?rhel} <= 7) || (0%{?fedora} && 0%{?fedora} <= 23) || 0%{?oreon}
%patch -P 0 -p1
%endif

%patch -P 1 -p1 -b .segfault_upload
%patch -P 2 -p1 -b .r1848298

%build
APXS=%{_httpd_apxs} ./configure.apxs
make

%install
%make_install MKINSTALLDIRS="mkdir -p"
mkdir -p %{buildroot}{%{_httpd_confdir},%{_httpd_modconfdir}}
echo "LoadModule fcgid_module modules/mod_fcgid.so" > %{buildroot}%{_httpd_modconfdir}/10-fcgid.conf
install -D -m 644 fcgid24.conf %{buildroot}%{_httpd_confdir}/fcgid.conf
install -d -m 755 %{buildroot}/run/mod_fcgid

# Include the manual as %%doc, don't need it elsewhere
rm -rf %{buildroot}%{_httpd_contentdir}/manual

# Make sure /run/mod_fcgid exists at boot time (#656625)
install -d -m 755 %{buildroot}%{_tmpfilesdir}
install -p -m 644 %{SOURCE4} %{buildroot}%{_tmpfilesdir}/mod_fcgid.conf

%files
%license LICENSE-FCGID
%doc README.RPM README.SELinux
# mod_fcgid.html.en is explicitly encoded as ISO-8859-1
%doc CHANGES-FCGID NOTICE-FCGID README-FCGID STATUS-FCGID
%doc docs/manual/mod/mod_fcgid.html.en modules/fcgid/ChangeLog
%doc build/fixconf.sed
%{_libdir}/httpd/modules/mod_fcgid.so
%config(noreplace) %{_httpd_modconfdir}/10-fcgid.conf
%config(noreplace) %{_httpd_confdir}/fcgid.conf
%{_tmpfilesdir}/mod_fcgid.conf
%dir %attr(0775,root,apache) /run/mod_fcgid/

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.3.9-37
- Import
