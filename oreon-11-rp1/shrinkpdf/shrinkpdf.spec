%global source0_hash 8040ee876411fdcfe8e74040f700dcf4fc2844a7e6f29c5041e8e73c34af9cd0

Name:           shrinkpdf
Version:        1.2
Release:        2%{?dist}
Summary:        Simple wrapper around Ghostscript to shrink PDFs

# License mentioned in README.md
License:        BSD-3-Clause
URL:            https://github.com/aklomp/%{name}
Source0:        %{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch:      noarch

%if 0%{?fedora} > 27
Requires:       ghostscript
%else
Requires:       ghostscript-core
%endif
Requires:       coreutils

%description
A simple wrapper around Ghostscript to shrink PDFs (as in reduce
file size) under Linux. The script feeds a PDF through Ghostscript,
which performs lossy recompression by such methods as downsampling
the images to the given resolution (default of 72 DPI). The result
should be (but not always is) a much smaller file.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{version}

%build

%install
install -p -m 0755 %{name}.sh -D %{buildroot}%{_bindir}/%{name}

%files
%doc README.md
%{_bindir}/%{name}

%changelog
%autochangelog
