%global source0_hash 75bdfeaa17e4af168fae2c262867b2992087aef39d8580965cb90d37a7d093c2
%global gem_name mustache
Name: rubygem-%{gem_name}
Version: 1.1.3
Release:        1%{?dist}
Summary:        Mustache is a framework-agnostic way to render logic-free views
License: MIT
URL: https://github.com/mustache/mustache
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Patch0: rubygem-mustache-1.1.1-Fix-test-race-condition.patch
BuildArch: noarch
# oreon:deps
BuildRequires:  ruby
BuildRequires:  ruby(release)
BuildRequires:  rubygem(minitest)
BuildRequires:  rubygem(ostruct)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
Inspired by ctemplate, Mustache is a framework-agnostic way to render
logic-free views.

As ctemplates says, "It emphasizes separating logic from presentation:
it is impossible to embed application logic in this template
language.

Think of Mustache as a replacement for your views. Instead of views
consisting of ERB or HAML with random helpers and arbitrary logic,
your views are broken into two parts: a Ruby class and an HTML
template.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch
%description doc
Documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n %{gem_name}-%{version}

%patch 0 -p1

%build

gem build ../%{gem_name}-%{version}.gemspec
%gem_install
%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/
mkdir -p %{buildroot}%{_bindir}
cp -a .%{_bindir}/* \
        %{buildroot}%{_bindir}/
find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x
mkdir -p %{buildroot}%{_mandir}/man5
cp -a .%{gem_instdir}/man/mustache.5 %{buildroot}%{_mandir}/man5
mkdir -p %{buildroot}%{_mandir}/man1
cp -a .%{gem_instdir}/man/mustache.1 %{buildroot}%{_mandir}/man1
cp -a .%{gem_instdir}/man/*.html .
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

pushd .%{gem_instdir}
sed -i '/simplecov/,/^end$/ s/^/#/' test/helper.rb
LANG=C.UTF-8 ruby -Ilib -e 'Dir.glob "./test/**/*_test.rb", &method(:require)'
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-mustache-doc -f %{oreon_filedir}/rubygem-mustache-doc.list

%changelog

%autochangelog
