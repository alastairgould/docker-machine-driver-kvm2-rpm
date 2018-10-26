Name:          docker-machine-driver-kvm2
Version:       0.30.0
Release:       1%{?dist}
Summary:       Minikube-maintained KVM driver for docker-machine

Group:         Development Tools
URL:           https://github.com/kubernetes/minikube
License:       ASL 2.0
Source0:       https://storage.googleapis.com/minikube/releases/v%{version}/%{name}
ExclusiveArch: x86_64

%description
Minikube-maintained KVM driver for docker-machine

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}/%{_bindir}
%{__install} -m 755 %{SOURCE0} %{buildroot}/%{_bindir}/%{name}

%files
%{_bindir}/%{name}
