%global source0_hash e10382ab75518bad8319eb922ad04f907cb20cccb451a3aa980c9d005e661acc

Name:           uthash
Version:        2.3.0
Release:        11%{?dist}
Summary:        A hash table for C structures

License:        BSD-1-Clause
URL:            http://troydhanson.github.io/%{name}
Source0:        https://github.com/troydhanson/uthash/archive/v2.3.0/uthash-2.3.0.tar.gz

BuildRequires:  asciidoc
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)

%description
Any C structure can be stored in a hash table using uthash.  Just
add a UT_hash_handle to the structure and choose one or more fields
in your structure to act as the key.  Then use these macros to store,
retrieve or delete items from the hash table.


%package devel
Summary:        A hash table for C structures (headers only)

# c-compiled libraries have been dropped upstream.
Obsoletes:      libut          < 2.3.0
Obsoletes:      libut-devel    < 2.3.0

Provides:       %{name}        = %{version}-%{release}
Provides:       %{name}-static = %{version}-%{release}
Provides:       libut          = %{version}-%{release}
Provides:       libut-devel    = %{version}-%{release}

BuildArch:      noarch

%description devel
Any C structure can be stored in a hash table using uthash.  Just
add a UT_hash_handle to the structure and choose one or more fields
in your structure to act as the key.  Then use these macros to store,
retrieve or delete items from the hash table.


%package tools
Summary:        Command-line utilities for %{name}
Requires:       %{name}        = %{version}-%{release}

%description tools
This package provides the hashscan and keystats utility programs
for %{name}.

The hashscan program examines a running process and reports on the
uthash tables that it finds in that program’s memory.  It can also
save the keys from each table in a format that can be fed into keystats.

The keystats program is able to analyze which hash function has the best
characteristics on the set of keys reported by the hashscan program.


%package doc
Summary:        Documentation-files for %{name}
BuildArch:      noarch
Requires:       %{name}        = %{version}-%{release}

%description doc
This package contains the documentation-files for %{name}.


%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -p1


%build
%set_build_flags
%make_build -C doc
%make_build -C tests
%make_build -C tests/threads


%install
mkdir -p %{buildroot}{%{_bindir},%{_includedir},%{_pkgdocdir}/html}
install -pm 0755 tests/{hashscan,keystats} %{buildroot}%{_bindir}
install -pm 0644 src/*.h %{buildroot}%{_includedir}
# Install doc.
install -pm 0644 doc/*.txt tests/example.c %{buildroot}%{_pkgdocdir}
install -pm 0644 doc/*.html doc/*.css doc/*.png %{buildroot}%{_pkgdocdir}/html
rm -f %{buildroot}%{_pkgdocdir}/html/google*.html


%files devel
%license LICENSE
%doc %dir %{_pkgdocdir}
%doc %{_pkgdocdir}/ChangeLog.txt
%{_includedir}/*.h


%files tools
%{_bindir}/*


%files doc
%doc %{_pkgdocdir}


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.3.0-11
- Prepare for Oreon 11 (RP1)
