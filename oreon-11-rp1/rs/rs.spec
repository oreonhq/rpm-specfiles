%global source0_hash 919215dc9fe85a27a30bf63d56406cfb503f9fc9820323c4bd3bfe75a6a3bc3f

Summary:        Reshape a data array
Name:           rs
Version:        20200313
Release:        10%{?dist}
# BSD-3-Clause (rs.c, rs.1), ISC (utf8.c, .linked/strtonum.c, reallocarray.c), MirOS (rs.h, check.pl)
License:        BSD-3-Clause AND ISC AND MirOS
URL:            https://man.openbsd.org/rs.1
Source0:        https://www.mirbsd.org/MirOS/dist/mir/%{name}/%{name}-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/MirBSD/mksh/bd8c18b7254d8735f18d239ca3fffaddc0434795/check.pl
BuildRequires:  gcc
BuildRequires:  perl-interpreter

%description
rs reads the standard input, interpreting each line as a row of blank-
separated entries in an array, transforms the array according to the
options, and writes it on the standard output. Numerous options control
input, reshaping and output processing; the simplest usage example is
"ls -1 | rs", which outputs the same (on an 80-column terminal) as the
modern "ls" with no "-1" argument.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p0 -n %{name}

%build
%{__cc} -DNEED_STRTONUM -I. -DMBSDPORT_H=\"rs.h\" -o %{name} $RPM_OPT_FLAGS $RPM_LD_FLAGS rs.c utf8.c .linked/strtonum.c

%install
install -D -p -m 0755 %{name} $RPM_BUILD_ROOT%{_bindir}/%{name}
install -D -p -m 0644 %{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1/%{name}.1

%check
perl %{SOURCE1} -s check.t -v -p ./rs

%files
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
%autochangelog
