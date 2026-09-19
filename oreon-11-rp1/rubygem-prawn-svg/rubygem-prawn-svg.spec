%global source0_hash b87031f946b730e4802fda0054971f292f755aee81e7a21c0a71669c646a1c32

%global gem_name prawn-svg

Name: rubygem-%{gem_name}
Version: 0.36.2
Release: 4%{?dist}
Summary: SVG renderer for Prawn PDF library
License: MIT
URL: http://github.com/mogest/prawn-svg
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# https://github.com/mogest/prawn-svg/commit/9538e0211ce0b38df9bb893c7698ea0e204ece2e
# Fix testsuite for rexml 3.4.3 and above
Patch0:  prawn-svg-0.36.2-testsuite-rexml-3_4_3.patch
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(rspec)
BuildRequires: rubygem(prawn)
BuildRequires: rubygem(css_parser)
BuildRequires: rubygem(rexml) >= 3.4.3
BuildArch: noarch

%description
This gem allows you to render SVG directly into a PDF using the 'prawn' gem. 
Since PDF is vector-based, you'll get nice scaled graphics if you use SVG
instead of an image.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n  %{gem_name}-%{version}
%patch -P0 -p1

%build
gem build ../%{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
pushd .%{gem_instdir}
# Don't use Bundler.
sed -i "/require 'bundler'/ s/^/#/" spec/spec_helper.rb
sed -i "/Bundler/ s/^/#/" spec/spec_helper.rb
rspec -rprawn-svg spec
popd

%files
%dir %{gem_instdir}
%doc %{gem_instdir}/README.md
%exclude %{gem_instdir}/.gitignore
%exclude %{gem_instdir}/.rspec
%exclude %{gem_instdir}/.github/
%exclude %{gem_instdir}/Gemfile.lock
%exclude %{gem_instdir}/.rubocop.yml
%exclude %{gem_instdir}/.rubocop_todo.yml
%license %{gem_instdir}/LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%exclude %{gem_instdir}/spec/sample_output
%{gem_instdir}/Gemfile
%{gem_instdir}/Rakefile
%{gem_instdir}/prawn-svg.gemspec
%{gem_instdir}/spec

%changelog
%autochangelog
