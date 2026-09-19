%global source0_hash b1da04a2915d1d057f3c2525e295ef15016a64e6667eac83a14641bbd83b9246

Name:           R-fastmap
Version:        %R_rpm_version 1.2.0
Release:        %autorelease
Summary:        Fast Data Structures

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  R-devel

%description
Fast implementation of data structures, including a key-value store, stack,
and queue. Environments are commonly used as key-value stores in R, but
every time a new key is used, it is added to R's global symbol table,
causing a small amount of memory leakage. This can be problematic in cases
where many different keys are used. Fastmap avoids this memory leak issue
by implementing the map using data structures in C++.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -c

%generate_buildrequires
%R_buildrequires

%build

%install
%R_install
%R_save_files

%check
%R_check

%files -f %{R_files}

%changelog
%autochangelog
