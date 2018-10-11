//
//  <#ClassName#>Controller.swift
//
//  Created by Beyond on 2018/6/6.
//  Copyright © 2018年 张东坡. All rights reserved.
//

import UIKit
import Moya
import Result
class <#ClassName#>ViewController: TWBaseViewController {
    //MARK: - Property
    var store: Store<<#ClassName#>Action, <#ClassName#>State, <#ClassName#>Command>!
    lazy var reducer = <#ClassName#>Reducer.init(owner: self)
    //MARK: - Life Cycle
    override func viewDidLoad() {
        super.viewDidLoad()
        store = Store<<#ClassName#>Action, <#ClassName#>State, <#ClassName#>Command>(reducer: reducer.reducer, initialState: <#ClassName#>State())
        store.subscribe  { [weak self] state, previousState, command in
            self?.stateDidChange(state: state, previousState: previousState, command: command)
        }
    }
    //MARK: - State Change
    private func stateDidChange(state: <#ClassName#>State, previousState: <#ClassName#>State, command: <#ClassName#>Command?) {
        if let command = command {
            switch command {
                //解析command,比如网络请求，跳转，弹窗操作。
            }
        }
         //通过 state 改变 view 状态
    }
    //MARK: - Private Method
    
    //MARK: - Public Method
    
    //MARK: - Action Event
    
}

