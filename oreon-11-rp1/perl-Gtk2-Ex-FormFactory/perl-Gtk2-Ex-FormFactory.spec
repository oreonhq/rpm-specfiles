%global source0_hash 576358725bb9df29b86a0f457c91355271ed3504520e857b869beafb41b56c8a

Name:           perl-Gtk2-Ex-FormFactory
Version:        0.67
Release:        40%{?dist}
Summary:        Framework for GTK2 Perl applications
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            http://www.exit1.org/Gtk2-Ex-FormFactory/
Source0:        http://www.exit1.org/packages/Gtk2-Ex-FormFactory/dist/Gtk2-Ex-FormFactory-%{version}.tar.gz
BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(strict)
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(Gtk2)
BuildRequires:  perl(Gtk2::SimpleList)
BuildRequires:  perl(Gtk2::SimpleMenu)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Scalar::Util)
# Time::Local not used by tests
# Tests:
BuildRequires:  perl(Test::More)

%description
This is a framework which tries to make building complex GUI's easy, by
offering these two main features:

Consistent looking GUI without the need to code resp. tune each widget by
hand. Instead you declare the structure of your GUI, connect it to the data of
your program (which should be a well defined set of objects) and control how
this structure is transformed into a specific layout in a very generic way.

Automatically keep widget and object states in synchronization (in both
directions), even with complex data structures with a lot of internal
dependencies, object nesting etc.

%{?perl_default_filter}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Gtk2-Ex-FormFactory-%{version}
# Convert encoding
for f in $(find lib/ -name *.pm) README tutorial/README; do
    cp -p ${f} ${f}.noutf8
    iconv -f ISO-8859-1 -t UTF-8 ${f}.noutf8 > ${f}
    touch -r ${f}.noutf8 ${f}
    rm ${f}.noutf8
done

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
chmod -R u+w $RPM_BUILD_ROOT/*

%check
make test

%files
%doc examples/ Changes LICENSE README tutorial/
%{perl_vendorlib}/Gtk2/
%{_mandir}/man3/*.3*

%changelog
%autochangelog
