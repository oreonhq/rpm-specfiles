%global source0_hash 300e8343f408547d6b17ac0b94653ca4b7c2ad3625335ddadf24e4fb3d07355e

# Generated from actionmailer-1.3.6.gem by gem2rpm -*- rpm-spec -*-
%global gem_name actionmailer

Name: rubygem-%{gem_name}
Epoch: 1
Version: 8.0.3
Release: 2%{?dist}
Summary: Email composition and delivery framework (part of Rails)
License: MIT
URL: https://rubyonrails.org
Source0: https://rubygems.org/gems/%{gem_name}-%{version}%{?prerelease}.gem
# git clone http://github.com/rails/rails.git && cd rails/actionmailer
# git archive -v -o actionmailer-8.0.3-tests.tar.gz v8.0.3 test/
Source1: actionmailer-%{version}%{?prerelease}-tests.tar.gz

# Let's keep Requires and BuildRequires sorted alphabeticaly
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby >= 3.2.0
BuildRequires: rubygem(activesupport) = %{version}
BuildRequires: rubygem(actionpack) = %{version}
BuildRequires: rubygem(activejob)  = %{version}
BuildRequires: rubygem(mail) >= 2.5.4
BuildArch: noarch

%description
Email on Rails. Compose, deliver, and test emails using the familiar
controller/view pattern. First-class support for multipart email and
attachments.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{epoch}:%{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version}%{?prerelease} -b1

%build
gem build ../%{gem_name}-%{version}%{?prerelease}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
( cd .%{gem_instdir}
cp -a %{builddir}/test .

mkdir ../tools
# Fake test_common.rb. It does not provide any functionality besides
# `force_skip` alias.
touch ../tools/test_common.rb
# Netiher strict_warnings.rb appears to be useful.
touch ../tools/strict_warnings.rb

ruby -Ilib:test -e 'Dir.glob "./test/**/*_test.rb", &method(:require)'
)

%files
%dir %{gem_instdir}
%license %{gem_instdir}/MIT-LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/README.rdoc

%changelog
%autochangelog
