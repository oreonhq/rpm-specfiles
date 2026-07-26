%global source0_hash 4c25cd78919272aebec0a7f8c126011bb5a4b5d87422807a3423216f0a17a868

Name:		moe
Version:	1.16
Release:	1%{?dist}
Summary:	A powerful clean text editor

License:	GPL-3.0-or-later
URL:		http://www.gnu.org/software/moe/moe.html
Source0:	http://ftp.gnu.org/gnu/moe/moe-%{version}.tar.lz
Patch0:		moe-1.13-configure.patch

BuildRequires: make
BuildRequires:	ncurses-devel lzip gcc-c++

%description
GNU Moe is a powerful, 8-bit clean, text editor for ISO-8859 and ASCII 
character encodings. It has a modeless, user-friendly interface, online 
help, multiple windows, unlimited undo/redo capability, unlimited line 
length, global search/replace (on all buffers at once), block operations, 
automatic indentation, word wrapping, filename completion, directory 
browser, duplicate removal from prompt histories, delimiter matching, etc.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P 0 -p0 -b .configure

%build
%configure
make %{?_smp_mflags}

%install
make install INSTALL="%{__install} -p" DESTDIR=$RPM_BUILD_ROOT
%{__install} -p -d $RPM_BUILD_ROOT%{_mandir}/man1 
%{__install} -p -m 644 ./doc/moe.1 $RPM_BUILD_ROOT%{_mandir}/man1/
rm -f $RPM_BUILD_ROOT%{_infodir}/dir

%files
%doc AUTHORS README NEWS ChangeLog
%license COPYING
%{_datadir}/info/%{name}.info*
%config(noreplace) %{_sysconfdir}/%{name}.conf
%{_bindir}/%{name}
%{_mandir}/man1/%{name}*

%changelog
%autochangelog
