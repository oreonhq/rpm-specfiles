%global source0_hash 2af79bed90e0bda52ae500d16e7e7022037fad10c487c317e7f0ff17ec4b14f5

Summary: High-performance implementation of a colorful cat
Name:    lolcat
Version: 1.5
Release: 5%{?dist}
Source:  https://github.com/jaseg/lolcat/archive/v%{version}/%{name}-%{version}.tar.gz
URL:     https://github.com/jaseg/lolcat/

Patch1:  lolcat-Makefile.patch

License: WTFPL
BuildRequires: make
BuildRequires: gcc

%description
lolcat is a colorful version of 'cat'. It is faster than python-lolcat 
and much faster than ruby-lolcat. It works well with "non-binary" 
characters, but who would want to display binary data!

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
%set_build_flags
%make_build all

%install
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
%make_install DESTDIR=$RPM_BUILD_ROOT/%{_bindir}

%files
%{_bindir}/lolcat
%{_bindir}/censor
%doc README.md
%license LICENSE

%changelog
%autochangelog
