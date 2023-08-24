%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
Name: kjournald
Version: 23.08.0
Release: 1
%if 0%{?git:1}
Source0:        https://invent.kde.org/system/%{name}/-/archive/master/%{name}-master.tar.bz2
%else
Source0:        https://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz
%endif
Summary: Graphical frontend for viewing the system journal
URL: https://github.com/kjournald/kjournald
License: GPL
Group: System
BuildRequires: cmake ninja

%description
Graphical frontend for viewing the system journal

%prep
%autosetup -p1
%cmake_kde5 -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build
%find_lang %{name}

%files -f %{name}.lang
%{_bindir}/kjournaldbrowser
%{_libdir}/libkjournald.so*
%{_datadir}/applications/org.kde.kjournaldbrowser.desktop
%{_datadir}/metainfo/org.kde.kjournaldbrowser.appdata.xml
%{_datadir}/qlogging-categories5/kjournald.categories