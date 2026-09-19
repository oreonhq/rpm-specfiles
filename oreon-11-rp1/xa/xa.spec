%global source0_hash 63c12a6a32a8e364f34f049d8b2477f4656021418f08b8d6b462be0ed3be3ac3

Name:           xa
Version:        2.4.1
Release:        5%{?dist}
Summary:        6502/65816 cross-assembler

License:        GPL-2.0-or-later
URL:            http://www.floodgap.com/retrotech/xa/
Source0:        http://www.floodgap.com/retrotech/%{name}/dists/%{name}-%{version}.tar.gz
# update the build system, reported in private email
Patch0:         %{name}-2.4.0-make.patch
BuildRequires:  make
BuildRequires:  gcc
# Perl needed for test-suite
BuildRequires:  perl-generators

%description
xa is a high-speed, two-pass portable cross-assembler. It understands
mnemonics and generates code for NMOS 6502s (such as 6502A, 6504, 6507,
6510, 7501, 8500, 8501, 8502 ...), CMOS 6502s (65C02 and Rockwell R65C02)
and the 65816.

Key amongst its features:

    * C-like preprocessor (and understands cpp for additional feature support)
    * rich expression syntax and pseudo-op vocabulary
    * multiple character sets
    * binary linking
    * supports o65 relocatable objects with a full linker and relocation suite, 
      as well as "bare" plain binary object files
    * block structure for label scoping 

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

# fix encoding
for f in ChangeLog
do
    iconv -f ISO-8859-1 -t UTF-8 < $f > $f.new
    touch -r $f $f.new
    mv $f.new $f
done

%build
%make_build CFLAGS="%{build_cflags}" LDFLAGS="%{build_ldflags}"

%check
make test

%install
%make_install PREFIX=%{_prefix} CFLAGS="%{build_cflags}" LDFLAGS="%{build_ldflags}"

%files
%doc COPYING ChangeLog README.1st
%{_bindir}/*
%{_mandir}/man1/*

%changelog
%autochangelog
