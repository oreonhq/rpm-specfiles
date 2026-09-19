%global source0_hash 9b2be5e9b9e66d715f956a7de4b4c3bc429ac1d1dbb58ec5ba3c923d0a9f59fd

Name:           sjasm
Version:        0.42c
Release:        9%{?dist}
Summary:        A z80 cross assembler
# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            http://www.xl2s.tk
Source0:        http://www.xl2s.tk/%{name}42c.zip
Patch0:         sjasm-0.42c-fixmakefile.patch
Patch1:         sjasm-0.42c-skipblanks.patch
Patch2:         sjasm-0.42c-cxx11.patch
Patch3:         sjasm-0.42c-cstring.patch
Patch4:         sjasm-0.42c-signedness.patch

BuildRequires:  make
BuildRequires:  gcc-c++

%description
SjASM is a two pass macro Z80 cross assembler

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qc
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p1
sed -i 's/\r//' %{name}.txt

# Convert to UTF8
iconv -f iso8859-1 %{name}.txt -t utf8 > %{name}.txt.conv \
    && /bin/mv -f %{name}.txt.conv %{name}.txt

%build
make -C sjasmsrc42c %{?_smp_mflags} CXXFLAGS="%{optflags} -DMAX_PATH=MAXPATHLEN"

%install
rm -rf %{buildroot}
make -C sjasmsrc42c install DESTDIR=%{buildroot}

%files
%{_bindir}/%{name}
%doc %{name}.txt

%changelog
%autochangelog
