%global source0_hash dc530018a4684512f8f38143cd2a096c9f02a1fc2459edcfe534787a7fc77d4b
%global source1_hash b69aa65951e5381fa807f347780030cfe557910427b5d26b9e0a309682186c8a
%global gem_name coderay
%if %{undefined rhel} || (0%{?oreon} >= 11)
%bcond_without shoulda
%endif
Name: rubygem-%{gem_name}
Version: 1.1.3
Release:        1%{?dist}
Summary:        Fast syntax highlighting for selected languages
License: MIT
URL: http://coderay.rubychan.de
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1: https://github.com/rubychan/coderay/archive/refs/tags/v%{version}.tar.gz#/%{gem_name}-%{version}-tests.txz
Patch0: rubygem-coderay-1.1.3-fix-tests-Array-on-ruby-3.0.patch
%if %{with shoulda}
%endif
BuildArch: noarch
# oreon:deps
BuildRequires:  ruby
BuildRequires:  ruby(release)
BuildRequires:  rubygem(rspec)
BuildRequires:  rubygem(test-unit)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
Fast and easy syntax highlighting for selected languages, written in Ruby.
Comes with RedCloth integration and LOC counter.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch
%description doc
Documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source1_hash}" = "none" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source1_hash}" || { echo "oreon: Source1 hash mismatch" >&2; exit 1; }; }
%setup -q -n %{gem_name}-%{version} -b 1
find %{_builddir} -mindepth 2 -type d \( -name test -o -name tests -o -name spec -o -name specs \) -exec cp -a {} %{_builddir}/ \;
%patch -P0 -p1

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
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

pushd .%{gem_instdir}
cp -r %{_builddir}/%{gem_name}-%{version}/spec .
cp -r %{_builddir}/%{gem_name}-%{version}/test .
for file in \
  spec/spec_helper.rb \
  test/executable/suite.rb \
  test/functional/for_redcloth.rb \
  test/functional/suite.rb \
  test/unit/suite.rb; do
  sed -i "/^require 'simplecov'/ s/^/#/" "${file}"
done
LANG=C.UTF-8
ruby ./test/functional/suite.rb
ruby ./test/functional/for_redcloth.rb
ruby ./test/unit/suite.rb
%if %{with shoulda}
ruby ./test/executable/suite.rb
%endif
rspec spec
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-coderay-doc -f %{oreon_filedir}/rubygem-coderay-doc.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.1.3-12
- Import
