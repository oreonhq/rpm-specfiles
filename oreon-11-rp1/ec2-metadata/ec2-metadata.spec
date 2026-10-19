%global source0_hash e320585b2455a879f201c6a0cc381a5b645ce1bd851c7946e12dc6513c07769d
Name:           ec2-metadata
Version:        0.1.1
Release:        1%{?dist}
Summary:        EC2 instance metadata query tool
License:        MIT
URL:            http://aws.amazon.com/code/1825
Source0:        http://s3.amazonaws.com/ec2metadata/ec2-metadata
Requires:       bash, curl
BuildArch:      noarch
# oreon:deps

# /oreon:deps
%description
A simple bash script that uses curl to query the EC2 instance metadata from
within an instance running in Amazon EC2 or another cloud provider with a
compatible metadata service.
 
%prep

# none

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/%{_bindir}
install -p -m 755 %{SOURCE0} $RPM_BUILD_ROOT/%{_bindir}/
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
