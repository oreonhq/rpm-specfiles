%global source1_hash d34c2913576e97c61038475835fe7dc56ec55c35b2efad0495cc32cdc787e3be
%global source0_hash 6e759246556145642ef832d670fc06f9bd8539159a0e600847a00291dd7aae0c
%global gem_name haml
Name: rubygem-%{gem_name}
Version: 5.2.2
Release:        1%{?dist}
Summary:        An elegant, structured (X)HTML/XML templating engine
License: MIT and WTFPL
URL: http://haml.info/
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1: https://github.com/haml/haml/archive/refs/tags/v5.2.2.tar.gz
Patch0:  rubygem-haml-5.2.2-explicit-ostruct-dep.patch
Patch1:  rubygem-haml-5.2.2-ruby34-hash-inspect-formatting-change.patch
BuildArch: noarch
# oreon:deps
BuildRequires:  ruby
BuildRequires:  ruby(release)
BuildRequires:  rubygem(activemodel)
BuildRequires:  rubygem(minitest)
BuildRequires:  rubygem(railties)
BuildRequires:  rubygem(temple)
BuildRequires:  rubygem(tilt)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
Haml (HTML Abstraction Markup Language) is a layer on top of HTML or XML
that's designed to express the structure documents in a non-repetitive,
elegant, easy way by using indentation rather than closing
tags and allowing Ruby to be embedded with ease.
It was originally envisioned as a plugin for Ruby on Rails, but it can
function as a stand-alone templating engine.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch
%description doc
Documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version} -b 1
find %{_builddir} -mindepth 2 -type d \( -name test -o -name tests -o -name spec -o -name specs \) -exec cp -a {} %{_builddir}/ \;
(
cd %{_builddir}
%patch 0 -p1
%patch 1 -p1
)

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
ln -s %{_builddir}/test .
sed -i '/[bB]undler/ s/^/#/' test/test_helper.rb
sed -i '/[Ss]imple[Cc]ov/ s/^/#/g' test/test_helper.rb
mv test/template_test.rb{,.disable}
sed -i '/def _run/ s/add_to_stack: true, &block/add_to_stack: true, has_strict_locals: false, \&block/' \
  test/helpers_for_rails_test.rb
ruby -Ilib:test -e '(Dir.glob("./test/*_test.rb") - %w[./test/options_test.rb]).each {|f| require f }'
ruby -Ilib:test -e 'require "./test/options_test.rb"'
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-haml-doc -f %{oreon_filedir}/rubygem-haml-doc.list

%changelog

%autochangelog
