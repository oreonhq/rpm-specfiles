%global source0_hash 94061c070baf0f195000473559a7fd4ec22a586bae8cf1c1aefae3fa836dfc42

Name:           mingw-crossreport
Version:        201406
Release:        24%{?dist}
Summary:        Analysis tool to help cross-compilation to Windows

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://fedoraproject.org/wiki/MinGW
Source0:        crossreport.pl
Source1:        README
Source2:        COPYING
Source3:        crossreport.db.xz
Source4:        update-crossreport-db.pl

BuildArch:      noarch

BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
%if 0%{?fedora} >= 19
BuildRequires:  perl-podlators
%endif

BuildRequires:  xz

# For nm and c++filt.
Requires:       binutils

%description
CrossReport is a tool to help you analyze the APIs used by a compiled
Linux program, in order to work out the effort required to
cross-compile that program for Windows, using the Fedora MinGW
cross-compiler.

The simplest way to use it is to point it at an existing Linux binary,
and then read the generated report.

What it does in more detail: It looks at the libraries and API calls
used by the Linux binary, and compares them to the libraries and API
calls that we currently support under the Fedora MinGW cross-compiler.
It then works out what is missing, and produces a report suggesting
the amount of work that needs to be done to port the program.  For
example, whether whole libraries need to be ported first, and/or how
to substitute individual calls to work on Windows.

%package -n mingw32-crossreport
Summary:        Analysis tool to help cross-compilation to Windows

%description -n mingw32-crossreport
CrossReport is a tool to help you analyze the APIs used by a compiled
Linux program, in order to work out the effort required to
cross-compile that program for Windows, using the Fedora MinGW
cross-compiler.

The simplest way to use it is to point it at an existing Linux binary,
and then read the generated report.

What it does in more detail: It looks at the libraries and API calls
used by the Linux binary, and compares them to the libraries and API
calls that we currently support under the Fedora MinGW cross-compiler.
It then works out what is missing, and produces a report suggesting
the amount of work that needs to be done to port the program.  For
example, whether whole libraries need to be ported first, and/or how
to substitute individual calls to work on Windows.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

# empty

%build
# empty

%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
install -m 0755 %{SOURCE0} $RPM_BUILD_ROOT%{_bindir}/mingw32-crossreport

# Install the database.
mkdir -p $RPM_BUILD_ROOT%{_datadir}/crossreport
xzcat %{SOURCE3} > $RPM_BUILD_ROOT%{_datadir}/crossreport/crossreport.db
chmod 0644 $RPM_BUILD_ROOT%{_datadir}/crossreport/crossreport.db

# Install documentation (manually).
mkdir -p $RPM_BUILD_ROOT%{_docdir}/%{name}
install -m 0644 %{SOURCE1} %{SOURCE2} $RPM_BUILD_ROOT%{_docdir}/%{name}

# Build the manpage from the source.
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
pod2man -c "CrossReport" -r "%{name}-%{version}" %{SOURCE0} \
  > $RPM_BUILD_ROOT%{_mandir}/man1/mingw32-crossreport.1

%files -n mingw32-crossreport
%doc %{_docdir}/%{name}/COPYING
%doc %{_docdir}/%{name}/README
%{_bindir}/mingw32-crossreport
%{_mandir}/man1/mingw32-crossreport.1*
%{_datadir}/crossreport/

%changelog
%autochangelog
