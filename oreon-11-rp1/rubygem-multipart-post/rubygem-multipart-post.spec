%global source1_hash 1064b5c7d39a85dc8734db368296c870ca03082ed389cf7b749741ba45989b31
%global source0_hash 462979de2971b8df33c2ee797fd497731617241f9dcd93960cc3caccb2dd13d8
%global gem_name multipart-post
Name: rubygem-%{gem_name}
Version: 2.2.3
Release:        1%{?dist}
Summary:        A multipart form post accessory for Net::HTTP
License: MIT
URL: https://github.com/socketry/multipart-post
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1: https://github.com/socketry/multipart-post/archive/refs/tags/v2.2.3.tar.gz
BuildArch: noarch
# oreon:deps
BuildRequires:  ruby
BuildRequires:  ruby(release)
BuildRequires:  rubygem(rspec)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
Adds a streamy multipart form post capability to Net::HTTP. Also supports other
methods besides POST.

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

%build

gem build ../%{gem_name}-%{version}.gemspec
%gem_install
%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

pushd .%{gem_instdir}
ln -s %{_builddir}/spec spec
sed -i '/bundler\/setup/ s/^/#/' spec/spec_helper.rb
rspec -rspec_helper spec
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-multipart-post-doc -f %{oreon_filedir}/rubygem-multipart-post-doc.list

%changelog

%autochangelog
