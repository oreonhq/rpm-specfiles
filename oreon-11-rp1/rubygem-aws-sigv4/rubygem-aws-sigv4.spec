%global source0_hash 746efa6929bf16ec88b2768f04c53841c987dd28137c864366c6d7d985ff183c
%global gem_name aws-sigv4
Name:           rubygem-%{gem_name}
Version:        1.0.2
Release:        1%{?dist}
Summary:        AWS Signature Version 4 library
License:        Apache-2.0
URL:            http://github.com/aws/aws-sdk-ruby
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1:        %{name}-%{version}-repo.tgz
Patch0:         %{name}-pr2179-ruby32-file_exists-removal.patch
BuildArch:      noarch
# oreon:deps
BuildRequires:  rubygem(rspec)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
Amazon Web Services Signature Version 4 signing library. Generates sigv4
signature for HTTP requests.

%package doc
Summary:        Documentation for %{name}
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
%description doc
Documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

gem unpack %{SOURCE0}

%setup -q -D -T -n %{gem_name}-%{version}
tar -xzf %{SOURCE1}
%patch -P0 -p3

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%build

gem build %{gem_name}.gemspec
%gem_install
%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

cp -pr spec/ ./%{gem_instdir}
pushd ./%{gem_instdir}
rspec -Ilib spec
rm -rf spec
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-aws-sigv4-doc -f %{oreon_filedir}/rubygem-aws-sigv4-doc.list

%changelog

%autochangelog
