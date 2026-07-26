%global source0_hash 2a1df6999f82f734716be460f7cf0b56bd0589c9b3d91ba392b941259578be75

Summary:   General-purpose stream-handling tool
Name:      cstream
Version:   3.2.1
Release:   %autorelease

License:   MIT
URL:       http://www.cons.org/cracauer/cstream.html
Source:    http://www.cons.org/cracauer/download/%{name}-%{version}.tar.gz
Patch2:    %{name}-%{version}-Wextra.patch
Patch3:    %{name}-%{version}-double-assignment.patch
Patch5:    %{name}-%{version}-meh.patch
Patch6:    %{name}-%{version}-Werror=tautological-compare.patch

BuildRequires:  gcc
BuildRequires: make
%description
cstream filters data streams, much like the UNIX tool dd(1).

It has a more traditional commandline syntax, support for precise
bandwidth limiting and reporting and support for FIFOs.

Data limits and throughput rate calculation will work for files > 4 GB.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P2 -p1 -b .Wextra
%patch -P3 -p1 -b .double-assignment
%patch -P5 -p1 -b .meh
%patch -P6 -p1 -b .Werror=autological-compare

%build
%{configure} INSTALL="%{__install} -p"
%make_build CFLAGS="%{optflags} -Wall -Wextra -Wno-unused-parameter -Werror"

%install
%make_install

%check
%{__make} %{?_smp_mflags} check installcheck DESTDIR="%{buildroot}"

%files
%doc CHANGES COPYRIGHT README TODO
%doc %{_mandir}/man1/cstream.1*
%{_bindir}/cstream

%changelog
%autochangelog
