%global source0_hash c897bbfa9848688982c6d5c30529fc29d68df0b9ff22ffa73bad89db73a7ce49
Name:        iverilog
Version:     13_0
%define uver 13_0
Release:        1%{?dist}
Summary:        Icarus Verilog is a verilog compiler and simulator
License:     GPL-2.0-only
URL:         https://github.com/steveicarus/iverilog
Source0:        https://github.com/steveicarus/%{name}/archive/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  bison
BuildRequires:  bzip2-devel
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  gperf
BuildRequires:  make
BuildRequires:  python3-sphinx
BuildRequires:  readline-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
Icarus Verilog is a Verilog compiler that generates a variety of
engineering formats, including simulation. It strives to be true
to the IEEE-1364 standard.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{uver}
# Clean junks from tarball
find . -type f -name ".git" -exec rm '{}' \;
rm -rf `find . -type d -name "autom4te.cache" -exec echo '{}' \;`

%build

%configure
%make_build
%make_build -C Documentation html
%install
%{__make}    prefix=%{buildroot}%{_prefix} \
             bindir=%{buildroot}%{_bindir} \
             libdir=%{buildroot}%{_libdir} \
             libdir64=%{buildroot}%{_libdir} \
             includedir=%{buildroot}%{_includedir} \
             mandir=%{buildroot}%{_mandir}  \
             pdfdir=%{buildroot}%{_pdfdir}/ivl/ \
             vpidir=%{buildroot}%{_libdir}/ivl/ \
             INSTALL="install -p" \
install
rm -rf Documentation/_build/html/.buildinfo
mkdir -p %{buildroot}%{_docdir}/%{name}
cp -r Documentation/_build/html %{buildroot}%{_docdir}/%{name}
%oreon_autofiles main

%check

make check
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
