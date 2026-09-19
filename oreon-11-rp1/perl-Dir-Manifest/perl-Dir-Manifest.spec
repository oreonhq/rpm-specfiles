%global source0_hash 84ff7226873d5e8656ec77344c0838c153a9f015b46b60e1fe8798bb2927e505

%define upstream_name    Dir-Manifest

%{?perl_default_filter}

Name:       perl-%{upstream_name}
Version:    0.6.1
Release:    18%{?dist}

Summary:    Load texts or blobs from a directory of files
License:    MIT
Url:        http://metacpan.org/release/%{upstream_name}
Source0:    https://cpan.metacpan.org/authors/id/S/SH/SHLOMIF/%{upstream_name}-%{version}.tar.gz

BuildRequires: perl(:VERSION) >= 5.14.0
BuildRequires: perl(Exporter)
BuildRequires: perl(File::Spec)
BuildRequires: perl(IO::Handle)
BuildRequires: perl(IPC::Open3)
BuildRequires: perl(Module::Build)
BuildRequires: perl(Moo)
BuildRequires: perl(Path::Tiny)
BuildRequires: perl(Socket)
BuildRequires: perl(Test::More)
BuildRequires: perl(blib)
BuildRequires: perl(parent)
BuildRequires: perl(strict)
BuildRequires: perl(warnings)
BuildRequires: perl-generators
BuildRequires: perl-interpreter
BuildArch:  noarch

%description
Here is the primary use case: you have several long texts (and/or binary
blobs) that you wish to load from the code (e.g: for the "want"/expected
values of tests) and you wish to conveniently edit them, track them and
maintain them. Using Dir::Manifest you can put each in a
separate file in a directory, create a manifest file listing all valid
filenames/key and then say something like 'my $text =
$dir->text("deal24solution.txt", {lf => 1})'. And hopefully it will be done
securely and reliably.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{upstream_name}-%{version}

%build
perl Build.PL --installdirs=vendor

./Build

%check
./Build test

%install
./Build install --destdir=%{buildroot} --create_packlist=0

%files
%license LICENSE
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*

%changelog
%autochangelog
