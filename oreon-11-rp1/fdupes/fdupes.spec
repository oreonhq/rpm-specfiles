%global source0_hash 527b27a39d031dcbe1d29a220b3423228c28366c2412887eb72c25473d7b1736

# Place rpm-macros into proper location.
%global macrosdir %(d=%{_rpmconfigdir}/macros.d; [ -d $d ] || d=%{_sysconfdir}/rpm; /bin/echo $d)

Name:           fdupes
Epoch:          1
Version:        2.4.0
Release:        3%{?dist}
Summary:        Finds duplicate files in a given set of directories

License:        MIT
URL:            https://github.com/adrianlopezroche/%{name}
Source0:        https://github.com/adrianlopezroche/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz
Source1:        macros.%{name}

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  pcre2-devel
BuildRequires:  sqlite-devel

%description
FDUPES is a program for identifying duplicate files residing within specified
directories.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

# From README.
%{__cat} << EOF > LICENSE
FDUPES Copyright (c) 1999-2022 Adrian Lopez

Permission is hereby granted, free of charge, to any person
obtaining a copy of this software and associated documentation files
(the "Software"), to deal in the Software without restriction,
including without limitation the rights to use, copy, modify, merge,
publish, distribute, sublicense, and/or sell copies of the Software,
and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
EOF

autoreconf -fiv

%build
%configure
%make_build

%install
%make_install
install -Dpm 0644 %{SOURCE1} %{buildroot}%{macrosdir}/macros.%{name}

%check
./%{name} testdir
./%{name} --omitfirst testdir
./%{name} --recurse testdir
./%{name} --size testdir

%files
%license CONTRIBUTORS LICENSE
%doc CHANGES README
%{_mandir}/man1/%{name}.1*
%{_mandir}/man7/%{name}*.7*
%{_bindir}/%{name}
%{macrosdir}/macros.fdupes

%changelog
%autochangelog
