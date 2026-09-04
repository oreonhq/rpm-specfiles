%global source0_hash e797a7c9b01e567307e317c576b49ab4168017e63eea4dba9ce3cb587e2f22c2

# Generated from rails-html-sanitizer-1.0.1.gem by gem2rpm -*- rpm-spec -*-
%global gem_name rails-html-sanitizer

Name: rubygem-%{gem_name}
Version: 1.7.1
Release: 1%{?dist}
Summary: This gem is responsible to sanitize HTML fragments in Rails applications
License: MIT
URL: https://github.com/rails/rails-html-sanitizer
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# Fix compatibility for minitest 6
Patch0:  rails-html-sanitizer-1.6.2-minitest6.patch
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(loofah)
BuildRequires: rubygem(minitest)
BuildRequires: rubygem(minitest-mock)
BuildArch: noarch

%description
This gem is responsible for sanitizing HTML fragments in Rails applications.
Specifically, this is the set of sanitizers used to implement the Action View
SanitizerHelper methods sanitize, sanitize_css, strip_tags and strip_links.

Rails HTML Sanitizer is only intended to be used with Rails applications. If
you need similar functionality but aren't using Rails, consider using the
underlying sanitization library Loofah directly.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version}
%patch -P0 -p1

%build
gem build ../%{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
( cd .%{gem_instdir}
ruby -Ilib -e 'Dir.glob "./test/**/*_test.rb", &method(:require)'
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
%doc %{gem_instdir}/README.md
%{gem_instdir}/test

%changelog
%autochangelog
